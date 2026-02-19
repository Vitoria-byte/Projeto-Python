import mysql.connector
from app.config import DB_CONFIG

def get_conexao():
    return mysql.connector.connect(**DB_CONFIG)
