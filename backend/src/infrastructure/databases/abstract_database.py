from abc import ABC, abstractmethod
import os
from psycopg2 import sql
# from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from config import DevelopmentConfig,Config, FactoryConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class AbstractDatabase(ABC):
    def __init__(self):
        env = os.getenv("FLASK_ENV", "development")
        config = FactoryConfig.get_config(env)

        self.database_uri = config.DATABASE_URI
        if not self.database_uri:
            raise ValueError("DATABASE_URI is not set. Check .env configuration")

        self.engine = create_engine(self.database_uri)
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
        self.session = self.SessionLocal()
