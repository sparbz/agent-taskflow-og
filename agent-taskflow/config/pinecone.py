import os
import pinecone
from dotenv import load_dotenv

# Load default environment variables (.env)
load_dotenv()

# Pinecone configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "")
TABLE_NAME = os.getenv("TABLE_NAME", "")

def init_pinecone():
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
    index = pinecone.Index(TABLE_NAME)
    return TABLE_NAME, index
