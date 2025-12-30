import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path='trade.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        # Таблица пользователей
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                qr_code TEXT UNIQUE,
                username TEXT,
                phone TEXT,
                email TEXT,
                reg_date TIMESTAMP
            )
        ''')
        
        # Таблица объявлений
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT,
                description TEXT,
                category TEXT,
                type TEXT,
                price TEXT,
                location TEXT,
                date TIMESTAMP,
                active INTEGER DEFAULT 1,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.conn.commit()
    
    # ... остальные методы из вашего кода ...
    
    def close(self):
        self.conn.close()
