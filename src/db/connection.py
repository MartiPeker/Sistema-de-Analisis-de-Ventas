from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.config import DB_CONFIG

class DBConnection:
    _instance = None
    _session_factory = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance._init_engine()
        return cls._instance

    def _init_engine(self):
        url = (
            f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
            f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        self.engine = create_engine(url, echo=False)
        self._session_factory = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        return self._session_factory()

    def close(self):
        self._session_factory.remove()