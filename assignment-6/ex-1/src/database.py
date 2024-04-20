import sqlite3

class Database(object):
    
    def __new__(cls, name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
            cls.instance.connection = sqlite3.connect(f'{name}.db')
        return cls.instance
    
    def connect(self):
        self.cursor = self.connection.cursor()
        
    def disconnect(self):
        self.cursor.close()
        
    def execute_query(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        
        self.connection.commit()
            
        return self.cursor.fetchall()
