import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables from .env file
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")  # Default URI for local Neo4j
