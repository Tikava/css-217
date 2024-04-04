from src.utils import Singleton
import psycopg2

class Database(Singleton):
    def __init__(self, dbname, user, password):
        self.database_name = dbname
        self.user = user
        self.connection = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    
    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        self.connection.commit()
        
    def get_connection_info(self):
        return {
            'database_name': self.database_name,
            'username': self.user
        }