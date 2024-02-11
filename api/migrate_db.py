"""migrate_db.py"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from api.models.models import Base
from api.seed import insert_seed_data

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(bind=engine)


def reset_database():
    """Reset the database."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
    insert_seed_data(session=Session())
