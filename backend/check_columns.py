import sqlite3
import os

db_path = r'c:\Users\salma\Downloads\smart-bank-v2-FIXED\smartbank_v2\storage\database\smart_bank.db'

def check_columns():
    if not os.path.exists(db_path):
        print(f"File not found: {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        tables = ['users', 'staff', 'admins', 'service_applications']
        for table in tables:
            print(f"\nColumns in {table}:")
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            for col in columns:
                print(f"  - {col[1]} ({col[2]})")
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_columns()
