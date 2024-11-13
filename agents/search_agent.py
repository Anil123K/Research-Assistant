
import arxiv
from agents.database_agent import DatabaseAgent
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD  

class SearchAgent:
    def __init__(self, query, max_results=5):
        """
        Initializes the SearchAgent.
        :param query: The search query (topic) to search for.
        :param max_results: The maximum number of results to fetch (default: 5).
        """
        self.query = query
        self.max_results = max_results
        # Initialize DatabaseAgent here
        self.db_agent = DatabaseAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)  

    def search(self):
        """
        Perform the search for the given query using the arxiv API and store results in Neo4j.
        :return: A list of papers retrieved based on the search.
        """
        try:
            # Construct the arxiv search query
            search = arxiv.Search(
                query=self.query,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate  # Sort results by submission date
            )

            results = []

            # Loop through the search results
            for result in search.results():
                # Extract authors and handle optional fields
                authors = [author.name for author in result.authors] if result.authors else []
                
                # Safely retrieve keywords (if available)
                keywords = getattr(result, 'keywords', [])  
                
                # Log the paper data for debugging purposes
                print(f"Found paper: {result.title}, Published: {result.published}, Authors: {authors}, Keywords: {keywords}")

                # Create a dictionary with paper details
                paper_data = {
                    'title': result.title,
                    'summary': result.summary,
                    'url': result.entry_id,
                    'published': result.published,
                    'authors': authors,
                    'keywords': keywords
                }

                # Store the paper data in Neo4j
                self.db_agent.store_paper(paper_data)  # Store the paper in the database
                results.append(paper_data)

            if not results:
                print("No papers found for this query.")  # Debugging line if no results are found

            return results

        except Exception as e:
            print(f"Error occurred while performing the search: {e}")
            return []

    def close(self):
        """
        Close the connection to the Neo4j database after the search is completed.
        """
        self.db_agent.close()  # Close the database connection when done
