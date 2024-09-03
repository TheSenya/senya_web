from sqlalchemy import create_engine, MetaData
from databases import Database
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/fastapidb")

# Set up database connection and metadata
database = Database(DATABASE_URL)
metadata = MetaData()

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
