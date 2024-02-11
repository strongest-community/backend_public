"""migrate_db.py"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from api.models.models import Base
import
load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(bind=engine)


def reset_database():
    """Reset the database."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def insert_seed_data():
    """Insert seed data into the database."""
    session = Session()
    # シードデータの挿入例
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")

    session.add(user1)
    session.add(user2)

    # ここに他のシードデータを挿入するコードを追加

    session.commit()
    session.close()


if __name__ == "__main__":
    reset_database()
