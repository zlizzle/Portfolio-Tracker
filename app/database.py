from sqlmodel import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./portfolio.db")
engine = create_engine(DATABASE_URL, echo=True)
