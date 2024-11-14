This project is an academic research paper assistant built using Large Language Models (LLMs), Streamlit, FastAPI, and Neo4j. 
It aims to help users retrieve, summarize, and interact with academic research papers. 
The assistant supports various functions such as topic-based paper retrieval, Q&A, and generating summaries or research ideas.

PROJECT SETUP

Prerequisites

Python 3.7 or higher                                                                                                                                                                       
Neo4j cloud setup                                                                                                                                                                          
pip upgraded to the latest version 

INSTALLTION

git clone <repository-url>

Set Up a Virtual Environment:                                                                                                                                                              
python -m venv research_assistant_env                                                                                                                                                      
source research_assistant_env/bin/activate  

Install Required Libraries:                                                                                                                                                                
pip install transformers streamlit fastapi neo4j uvicorn outlines                                                                                                                          

RUNNING THE APPLICATION

streamlit run app.py

FEATURES

Retrieve Papers by Topic: Fetches papers from Neo4j based on the specified topic.                                                                                                          
Question Answering on Paper Summaries: Uses a DistilBERT model for answering questions directly from the paper summaries.                                                                  
Detailed and Contextualized Answers: Provides an elaborated answer with context from the paper, making responses more conversational and informative.                                      
Summarize Findings: Creates a summary of key insights from multiple papers related to a given topic.                                                                                       
Generate Future Research Directions: Identifies and compiles future research opportunities based on the content of the papers.                                                             



