from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

url=os.environ.get("DATABASE_URL")
#print(f"Database URL: {url}")
if url is None:
    raise NotImplementedError("DATABASE_URL environment variable not set")

engine=create_engine(url, echo=True)
# Access the database
def init_db():
    print("Accessing database")
    SQLModel.metadata.create_all(engine)
    print("Database Accessed")

# create the session
def get_session():
    with Session(engine) as session:
        yield session
