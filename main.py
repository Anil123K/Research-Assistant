from agents.search_agent import SearchAgent
from agents.database_agent import DatabaseAgent
from config import NEO4J_URI

def main():
    # Initialize the search and database agents
    search_agent = SearchAgent("machine learning")
    db_agent = DatabaseAgent(NEO4J_URI)
    
    # Fetch papers using the search agent
    papers = search_agent.search()
    
    if not papers:
        print("No papers found.")
    else:
        # Store papers in the database
        for paper in papers:
            db_agent.store_paper(paper)
        
        print("Papers stored successfully.")

    # Close the database connection
    db_agent.close()

if __name__ == "__main__":
    main()
