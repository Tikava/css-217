import sqlite3

class DataStorage:
    _instance = None

    def __new__(cls, db_file="data.db"):
        if cls._instance is None:
            cls._instance = super(DataStorage, cls).__new__(cls)
            cls._instance.db_file = db_file
            cls._instance.conn = None
        return cls._instance

    def connect(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.db_file)

    def store_text(self, text):
        self.connect()
        c = self.conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS text_info
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')

        c.execute("INSERT INTO text_info (text) VALUES (?)", (text,))
        self.conn.commit()

    def store_audio(self, name, artists, album, preview_url):
        self.connect()
        c = self.conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS audio_info
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, artists TEXT, album TEXT, preview_url TEXT)''')

        c.execute("INSERT INTO audio_info (name, artists, album, preview_url) VALUES (?, ?, ?, ?)",
                (name, ', '.join(artists), album, preview_url))
        self.conn.commit()

    def store_video(self, name, artists, album, preview_url):
        self.connect()
        c = self.conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS video_info
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, artists TEXT, album TEXT, preview_url TEXT)''')

        c.execute("INSERT INTO video_info (name, artists, album, preview_url) VALUES (?, ?, ?, ?)",
                (name, ', '.join(artists), album, preview_url))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
