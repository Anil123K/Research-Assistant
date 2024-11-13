# import streamlit as st
# from agents.search_agent import SearchAgent
# from agents.database_agent import DatabaseAgent
# from agents.qna_agent import QnAAgent

# # Database credentials
# NEO4J_URI = "neo4j+s://36329fac.databases.neo4j.io:7687"
# NEO4J_USER = "neo4j"
# NEO4J_PASSWORD = "O3YwKV_mWAF6nn1t4bZYZ6iQXr91XBMGRgzqWrzZ9Gw"

# # Initialize database agent
# db_agent = DatabaseAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

# # Streamlit UI
# st.title("Academic Research Paper Assistant")

# # Step 1: Topic Search
# st.header("Search for Research Papers")
# topic = st.text_input("Enter a research topic:")
# if st.button("Search"):
#     if topic:
#         search_agent = SearchAgent(topic, max_results=5)
#         papers = search_agent.search()

#         # Store papers in Neo4j
#         for paper in papers:
#             db_agent.store_paper(paper)
        
#         st.success(f"Found and stored {len(papers)} papers related to '{topic}'.")
#         st.write("Papers:")
#         for paper in papers:
#             st.write(f"- {paper['title']}")

# # Step 2: Q&A Interface
# st.header("Ask Questions About the Topic")
# question = st.text_input("Enter your question:")
# if st.button("Ask"):
#     if question:
#         qna_agent = QnAAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
#         try:
#             # Get the answer
#             # Here, we're assuming that the latest stored papers are relevant
#             answer, paper_id = qna_agent.answer_question(question, paper_id=None)
#             st.write("Answer:", answer)
#             st.write(f"Source: Paper ID {paper_id}")
#         finally:
#             qna_agent.close()

# # Close the database connection at the end
# db_agent.close()


# import streamlit as st
# from agents.database_agent import DatabaseAgent
# from agents.search_agent import SearchAgent
# from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# def main():
#     # Initialize DatabaseAgent
#     db_agent = DatabaseAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

#     st.title("Research Assistant")
#     topic = st.text_input("Enter a topic to search for papers")
    
#     if st.button("Search"):
#         # Initialize SearchAgent and perform search
#         search_agent = SearchAgent(topic, max_results=5)
#         papers = search_agent.search()
        
#         if papers:
#             st.write(f"Found {len(papers)} papers on the topic '{topic}':")
            
#             # Store each paper in Neo4j and display it in the UI
#             for paper in papers:
#                 db_agent.store_paper(paper)
#                 st.write(f"**Title**: {paper['title']}")
#                 st.write(f"**URL**: {paper['url']}")
#                 st.write(f"**Published on**: {paper['published']}")
#                 st.write(f"**Summary**: {paper['summary']}")
#                 st.write("---")
#         else:
#             st.write("No papers found for this topic.")

#     db_agent.close()

# if __name__ == "__main__":
#     main()

# import streamlit as st
# from agents.search_agent import SearchAgent

# # Streamlit UI for user input
# st.title("Research Paper Search")

# # Input box to capture the topic from the user
# topic = st.text_input("Enter topic to search for:")

# # Button to trigger the search
# if st.button("Search"):
#     if topic:
#         try:
#             # Initialize the SearchAgent with the user-provided topic
#             agent = SearchAgent(query=topic)
#             papers = agent.search()

#             if not papers:
#                 st.write("No papers found.")
#             else:
#                 # Display search results
#                 for paper in papers:
#                     st.write(f"**Title**: {paper['title']}")
#                     st.write(f"[Link to Paper]({paper['url']})")
#                     st.write(f"**Published on**: {paper['published']}")
#                     st.write(f"**Summary**: {paper['summary']}")
#                     st.write("-" * 50)

#             agent.close()  # Ensure the database connection is closed after use

#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#     else:
#         st.warning("Please enter a topic to search.")


# import streamlit as st
# from agents.search_agent import SearchAgent
# from agents.qna_agent import QnAAgent
# from agents.database_agent import DatabaseAgent
# from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# # Initialize DatabaseAgent
# db_agent = DatabaseAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

# # Streamlit UI
# st.title("Research Paper Search & QnA")

# # Step 1: Topic Search
# topic = st.text_input("Enter topic to search for:")

# if st.button("Search"):
#     if topic:
#         try:
#             # Initialize SearchAgent with the user-provided topic
#             search_agent = SearchAgent(query=topic)
#             papers = search_agent.search()

#             if not papers:
#                 st.write("No papers found.")
#             else:
#                 # Display search results
#                 st.write(f"Found {len(papers)} papers on the topic '{topic}':")
                
#                 # Store papers in the Neo4j database
#                 for paper in papers:
#                     db_agent.store_paper(paper)
#                     st.write(f"**Title**: {paper['title']}")
#                     st.write(f"[Link to Paper]({paper['url']})")
#                     st.write(f"**Published on**: {paper['published']}")
#                     st.write(f"**Summary**: {paper['summary']}")
#                     st.write("-" * 50)

#             # Close the agent connection after search
#             search_agent.close()

#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#     else:
#         st.warning("Please enter a topic to search.")

# # Step 2: Q&A Interface
# st.header("Ask Questions About the Papers")

# question = st.text_input("Enter your question:")

# if st.button("Ask"):
#     if question:
#         try:
#             # Initialize QnAAgent
#             qna_agent = QnAAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
            
#             # Retrieve the answer based on stored papers in the database
#             answer = qna_agent.answer_question(question, topic)
#             st.write("Answer:", answer)
            
#             # Close the QnA agent connection
#             qna_agent.close()
#         except Exception as e:
#             st.error(f"An error occurred while fetching the answer: {e}")
#     else:
#         st.warning("Please enter a question to ask.")

# # Close the database connection at the end
# db_agent.close()



import streamlit as st
from agents.search_agent import SearchAgent
from agents.qna_agent import QnAAgent
from agents.database_agent import DatabaseAgent

# Database credentials
NEO4J_URI = "neo4j+s://36329fac.databases.neo4j.io:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "O3YwKV_mWAF6nn1t4bZYZ6iQXr91XBMGRgzqWrzZ9Gw"

# Initialize database agent
db_agent = DatabaseAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

# Streamlit UI for user input
st.title("Research Paper Q&A")

# Initialize conversation history in session state if not present
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Step 1: Input for the topic
topic = st.text_input("Enter the topic to search for papers:")

# Step 2: Search for papers and display them
if topic:
    search_agent = SearchAgent(query=topic)
    papers = search_agent.search()

    if papers:
        st.write(f"Found {len(papers)} papers related to '{topic}':")
        for paper in papers:
            st.write(f"**Title**: {paper['title']}")
            st.write(f"[Link to Paper]({paper['url']})")
            st.write(f"**Published on**: {paper['published']}")
            st.write(f"**Summary**: {paper['summary']}")
            st.write("---")

        # Store the papers in the database after displaying
        for paper in papers:
            db_agent.store_paper(paper)

        # Show ongoing conversations
        for idx, conv in enumerate(st.session_state.conversation):
            st.write(f"**User:** {conv['question']}")
            st.write(f"**Bot:** {conv['answer']}")
            st.write("---")

        # Step 3: Input box for user to ask a question
        question_input = st.text_input("Ask a question about the papers:")

        # Button for submitting question
        if st.button("Ask") and question_input:
            # Initialize QnA agent for the question
            qna_agent = QnAAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

            # Get the answer from the QnA agent based on the topic and question
            try:
                answer = qna_agent.answer_question(question_input, topic)

                # Check if the answer is at least 50 words
                if len(answer.split()) < 50:
                    answer += " Let me elaborate further: " + qna_agent.elaborate_answer(question_input, topic)

                # Make the answer more conversational
                conversational_answer = f"Here's what I found on your question about {topic}: {answer}. Let me know if you'd like more details!"

                # Display the answer
                st.write(f"**Answer**: {conversational_answer}")

                # Append the question and answer to the conversation history
                st.session_state.conversation.append({"question": question_input, "answer": conversational_answer})

                # Clear the question input field for the next question
                st.session_state.question_input = ""

            except Exception as e:
                st.error(f"An error occurred while fetching the answer: {e}")
            finally:
                qna_agent.close()

    else:
        st.write("No papers found for this topic.")

else:
    st.write("Please enter a topic to search for papers first.")

# Close the database connection at the end
db_agent.close()

# ***********************************************************

# import streamlit as st
# from agents.search_agent import SearchAgent
# from agents.qna_agent import QnAAgent
# from agents.database_agent import DatabaseAgent

# # Database credentials
# NEO4J_URI = "neo4j+s://36329fac.databases.neo4j.io:7687"
# NEO4J_USER = "neo4j"
# NEO4J_PASSWORD = "O3YwKV_mWAF6nn1t4bZYZ6iQXr91XBMGRgzqWrzZ9Gw"

# # Initialize database agent
# db_agent = DatabaseAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

# # Streamlit UI for user input
# st.title("Research Paper Q&A")

# # Initialize conversation history in session state if not present
# if 'conversation' not in st.session_state:
#     st.session_state.conversation = []

# # Step 1: Input for the topic
# topic = st.text_input("Enter the topic to search for papers:")

# # Step 2: Search for papers and display them
# if topic:
#     # Initialize SearchAgent with the topic
#     search_agent = SearchAgent(query=topic)

#     # Fetch papers based on the query
#     papers = search_agent.search()

#     if papers:
#         st.write(f"Found {len(papers)} papers related to '{topic}':")
#         for paper in papers:
#             st.write(f"**Title**: {paper['title']}")
#             st.write(f"[Link to Paper]({paper['url']})")
#             st.write(f"**Published on**: {paper['published']}")
#             st.write(f"**Summary**: {paper['summary']}")
#             st.write("---")

#         # Store the papers in the database after displaying them
#         for paper in papers:
#             db_agent.store_paper(paper)

#         # Show ongoing conversations
#         for idx, conv in enumerate(st.session_state.conversation):
#             st.write(f"**User:** {conv['question']}")
#             st.write(f"**Bot:** {conv['answer']}")
#             st.write("---")

#         # Step 3: Input box for user to ask a question
#         question_input = st.text_input("Ask a question about the papers:")

#         # Button for submitting question
#         if st.button("Ask") and question_input:
#             # Initialize QnA agent for the question
#             qna_agent = QnAAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

#             try:
#                 # Get the answer from the QnA agent based on the topic and question
#                 answer = qna_agent.answer_question(question_input, topic)

#                 # Check if the answer is at least 50 words
#                 if len(answer.split()) < 50:
#                     answer += " Let me elaborate further: " + qna_agent.elaborate_answer(question_input, topic)

#                 # Make the answer more conversational
#                 conversational_answer = f"Here's what I found on your question about {topic}: {answer}. Let me know if you'd like more details!"

#                 # Display the answer
#                 st.write(f"**Answer**: {conversational_answer}")

#                 # Append the question and answer to the conversation history
#                 st.session_state.conversation.append({"question": question_input, "answer": conversational_answer})

#             except Exception as e:
#                 st.error(f"An error occurred while fetching the answer: {e}")
#             finally:
#                 qna_agent.close()

#     else:
#         st.write("No papers found for this topic.")
# else:
#     st.write("Please enter a topic to search for papers first.")

# # Close the database connection at the end
# db_agent.close()
