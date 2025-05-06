# app.py
from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL 데이터베이스 연결 설정
db_config = {
    'host': 'db',  # Docker Compose에서 설정한 서비스 이름 사용
    'user': 'root',
    'password': 'password',
    'database': 'test_db'
}

@app.route('/')
def hello_world():
    try:
        # MySQL 연결
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT message FROM greetings WHERE id=1")
        result = cursor.fetchone()
        return f"Hello, {result[0]} from Docker Compose!"
    except mysql.connector.Error as err:
        return f"Error: {err}"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=30309)
