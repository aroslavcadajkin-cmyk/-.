import uuid
from datetime import datetime

def generate_qr_code():
    """Генерация уникального QR-кода"""
    return str(uuid.uuid4())[:8]

def validate_email(email):
    """Простая валидация email"""
    return '@' in email and '.' in email

def format_date(date_string):
    """Форматирование даты для отображения"""
    if isinstance(date_string, str):
        return date_string[:10]
    return date_string

def create_test_user(db):
    """Создание тестового пользователя если нет"""
    db.cursor.execute("SELECT * FROM users WHERE username='Тестовый'")
    user = db.cursor.fetchone()
    
    if not user:
        qr = generate_qr_code()
        db.cursor.execute('''
            INSERT INTO users (qr_code, username, phone, email, reg_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (qr, 'Тестовый', '+79990000000', 'test@test.com', datetime.now()))
        db.conn.commit()
        return db.cursor.lastrowid, 'Тестовый'
    
    return user[0], user[2]
