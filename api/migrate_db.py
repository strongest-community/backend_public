"""migrate_db.py"""

import os
from sqlalchemy import create_engine

from dotenv import load_dotenv
from api.models.models import Base

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, echo=True)


def reset_database():
    """Reset the database."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
