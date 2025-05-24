import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

def get_url():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(get_url())
Session = sessionmaker(bind=engine)
session = Session()
