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

    def store_article(self, title, authors, publication_year, abstract, doi, journal, volume, issue, pages, keywords):
        self.connect()
        c = self.conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS articles
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT, 
                    authors TEXT,
                    publication_year INTEGER,
                    abstract TEXT,
                    doi TEXT,
                    journal TEXT,
                    volume INTEGER,
                    issue INTEGER,
                    pages TEXT,
                    keywords TEXT)''')

        c.execute("INSERT INTO articles (title, authors, publication_year, abstract, doi, journal, volume, issue, pages, keywords) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (title, authors, publication_year, abstract, doi, journal, volume, issue, pages, keywords))
        
        self.conn.commit()
        self.conn.close()

    def store_audio(self, name, artists, album, preview_url):
        self.connect()
        c = self.conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS audio_info
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, artists TEXT, album TEXT, preview_url TEXT)''')

        c.execute("INSERT INTO audio_info (name, artists, album, preview_url) VALUES (?, ?, ?, ?)",
                (name, ', '.join(artists), album, preview_url))
        self.conn.commit()

    def store_video(self, title, description, channel_title, published_at):
        self.connect()
        c = self.conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS video_info
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, channel_title TEXT, published_at TEXT)''')

        c.execute("INSERT INTO video_info (title, description, channel_title, published_at) VALUES (?, ?, ?, ?)",
                (title, description, channel_title, published_at))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
