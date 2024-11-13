
from neo4j import GraphDatabase
from transformers import pipeline

class QnAAgent:
    def __init__(self, uri, user, password):
        """
        Initializes the connection to Neo4j and Hugging Face model.
        :param uri: The Neo4j URI.
        :param user: The Neo4j user.
        :param password: The Neo4j password.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        # Load QA model (DistilBERT trained on SQuAD for question answering)
        self.qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def close(self):
        """
        Closes the connection to the Neo4j database.
        """
        self.driver.close()

    def get_papers_for_topic(self, topic):
        """
        Retrieves papers related to a specific topic from Neo4j.
        :param topic: The topic to search for.
        :return: A list of paper dictionaries.
        """
        with self.driver.session() as session:
            query = (
                "MATCH (p:Paper) "
                "WHERE p.title CONTAINS $topic OR p.summary CONTAINS $topic "
                "RETURN p.title AS title, p.summary AS summary, p.url AS url"
            )
            result = session.run(query, topic=topic)
            papers = [{"title": record["title"], "summary": record["summary"], "url": record["url"]} for record in result]
            return papers

    def elaborate_answer(self, answer, paper):
        """
        Elaborates the answer to make it more conversational and detailed.
        :param answer: The short answer text.
        :param paper: The paper information dictionary.
        :return: An elaborated response with more context.
        """
        return (
            f"Based on the paper titled '{paper['title']}', here’s what I found: {answer}. "
            f"This paper provides valuable insights into this topic. You can read the full paper [here]({paper['url']}). "
            f"Let me know if you'd like to explore other aspects of this topic!"
        )

    def answer_question(self, question, topic):
        """
        Answer a question based on papers related to the given topic.
        :param question: The user's question.
        :param topic: The topic related to the question.
        :return: The most relevant answer.
        """
        # Retrieve relevant papers from the database
        papers = self.get_papers_for_topic(topic)

        if not papers:
            return "I couldn’t find any papers related to this topic. Please try a different query."

        # For each paper, attempt to answer the question based on its summary
        answers = []
        for paper in papers:
            context = paper['summary']
            # Run the QA model on the context (summary of the paper)
            result = self.qa_model(question=question, context=context)
            answers.append({
                "answer": result['answer'],
                "score": result['score'],
                "title": paper['title'],
                "url": paper['url'],
                "context": context[:300]  
            })

        # Sort answers by score (descending) to get the most relevant answer
        answers = sorted(answers, key=lambda x: x['score'], reverse=True)
        top_answer = answers[0] if answers else {"answer": "No answer found.", "title": "N/A", "url": "#"}

        # Elaborate the answer to make it more conversational
        detailed_answer = self.elaborate_answer(top_answer['answer'], top_answer)

        
        seen_papers = set()

        # Add the detailed answer part with top papers
        detailed_answer += "\n\nHere are the top papers that contributed to this answer:\n"

        for answer in answers:
            # Check if the paper has already been added
            paper_title = answer['title']
    
    
            if paper_title not in seen_papers:
             
        # Add the paper title to the set and include it in the answer
             seen_papers.add(paper_title)
             detailed_answer += f"- From the paper '{paper_title}': {answer['answer']} [More info here]({answer['url']})\n"

             return detailed_answer

    def summarize_findings(self, topic):
        """
        Summarizes findings from multiple papers on the given topic.
        :param topic: The topic related to the question.
        :return: A summary of the findings from multiple papers.
        """
        papers = self.get_papers_for_topic(topic)
        if not papers:
            return "No papers found for this topic."

        summary = "Summary of findings from multiple papers:\n"
        for paper in papers:
            summary += f"- Paper: {paper['title']}\nSummary: {paper['summary'][:300]}...\n\n"
        return summary

    def generate_future_work(self, topic):
        """
        Generates ideas for future work based on the papers related to the given topic.
        :param topic: The topic related to the question.
        :return: Future work ideas extracted from the papers.
        """
        papers = self.get_papers_for_topic(topic)
        if not papers:
            return "No papers found for this topic."

        future_work_ideas = "Ideas for future work:\n"
        for paper in papers:
            if 'future work' in paper['summary'].lower():
                future_work_ideas += f"- Paper '{paper['title']}': {paper['summary'][:300]}...\n"
        return future_work_ideas

    def create_review_paper(self, topic):
        """
        Creates a well-structured review paper summarizing future research opportunities.
        :param topic: The topic related to the question.
        :return: A summary of research opportunities based on the papers.
        """
        papers = self.get_papers_for_topic(topic)
        if not papers:
            return "No papers found for this topic."

        review_paper = "Review Paper on Future Research Opportunities:\n"
        for paper in papers:
            review_paper += f"- Paper: {paper['title']}\nSummary: {paper['summary'][:300]}...\n\n"
        review_paper += "Future work and open questions remain, such as ..."
        return review_paper

    def generate_improvement_plan(self, topic):
        """
        Generate an improvement plan based on key research works, including novel contributions.
        :param topic: The topic related to the question.
        :return: An improvement plan based on the papers.
        """
        papers = self.get_papers_for_topic(topic)
        if not papers:
            return "No papers found for this topic."

        improvement_plan = "Improvement Plan based on Key Research Works:\n"
        for paper in papers:
            improvement_plan += f"- Paper: {paper['title']} - Key Contributions: {paper['summary'][:300]}...\n"
        improvement_plan += "Based on these contributions, further improvements could focus on ..."
        return improvement_plan


# Example usage
if __name__ == "__main__":
    uri = "neo4j+s://36329fac.databases.neo4j.io:7687"
    user = "neo4j"
    password = "O3YwKV_mWAF6nn1t4bZYZ6iQXr91XBMGRgzqWrzZ9Gw"

    # Initialize the QnAAgent
    qna_agent = QnAAgent(uri, user, password)

    # Ask a question related to a stored topic
    topic = "machine learning"
    question = "What are the recent advancements in machine learning?"
    answer = qna_agent.answer_question(question, topic)  # Get an answer based on the stored papers
    print(answer)

    # Get a summary of multiple papers on the topic
    summary = qna_agent.summarize_findings(topic)
    print(summary)

    # Generate ideas for future work on the topic
    future_work = qna_agent.generate_future_work(topic)
    print(future_work)

    # Create a review paper based on the topic
    review_paper = qna_agent.create_review_paper(topic)
    print(review_paper)

    # Generate an improvement plan based on the research works
    improvement_plan = qna_agent.generate_improvement_plan(topic)
    print(improvement_plan)

    # Close the connection to the database
    qna_agent.close()
