import unittest
from src.db.connection import DBConnection

class TestDBConnection(unittest.TestCase):
    def test_singleton(self):
        conn1 = DBConnection()
        conn2 = DBConnection()
        self.assertIs(conn1, conn2)

    def test_session_creation(self):
        conn = DBConnection()
        session = conn.get_session()
        self.assertIsNotNone(session)
        session.close()

if __name__ == "__main__":
    unittest.main()