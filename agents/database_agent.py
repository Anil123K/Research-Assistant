
from neo4j import GraphDatabase
from config import NEO4J_USER, NEO4J_PASSWORD, NEO4J_URI  

class DatabaseAgent:
    def __init__(self, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD):
        """
        Initializes the connection to the Neo4j database using the provided credentials.
        :param NEO4J_URI: The URI of the Neo4j database.
        :param NEO4J_USER: The username for Neo4j.
        :param NEO4J_PASSWORD: The password for Neo4j.
        """
        try:
            self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
            print("Connected to Neo4j database.")
        except Exception as e:
            print(f"Failed to connect to Neo4j database: {e}")
            self.driver = None

    def close(self):
        """
        Closes the connection to the Neo4j database.
        """
        if self.driver:
            self.driver.close()
            print("Connection to Neo4j closed.")
        else:
            print("No active database connection to close.")

    def store_paper(self, paper_data):
        """
        Stores a paper's data in the Neo4j database.
        :param paper_data: A dictionary containing paper information (title, summary, URL, etc.).
        """
        if not self.driver:
            print("No database connection available.")
            return

        with self.driver.session() as session:
            try:
                session.write_transaction(self._create_paper_node, paper_data)
                print(f"Paper '{paper_data['title']}' stored successfully.")
            except Exception as e:
                print(f"Failed to store paper '{paper_data['title']}': {e}")

    @staticmethod
    def _create_paper_node(tx, paper_data):
        """
        Cypher query to create a Paper node in the Neo4j database.
        :param tx: The transaction object.
        :param paper_data: A dictionary containing paper data to be stored.
        """
        query = (
            "CREATE (p:Paper {title: $title, summary: $summary, url: $url, published: $published, "
            "authors: $authors, keywords: $keywords})"
        )
        # Adding optional authors and keywords
        tx.run(query, title=paper_data['title'], summary=paper_data['summary'], 
               url=paper_data['url'], published=paper_data['published'], 
               authors=paper_data.get('authors', []), keywords=paper_data.get('keywords', []))

