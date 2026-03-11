import sqlite3
import os

db_path = r'c:\Users\salma\Downloads\smart-bank-v2-FIXED\smartbank_v2\storage\database\smart_bank.db'

def check_db():
    if not os.path.exists(db_path):
        print(f"File not found: {db_path}")
        return

    output = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [t[0] for t in cursor.fetchall()]
        output.append(f"Tables in database ({os.path.getsize(db_path)} bytes):")
        
        for name in tables:
            cursor.execute(f"SELECT COUNT(*) FROM \"{name}\"")
            count = cursor.fetchone()[0]
            output.append(f" - {name}: {count} rows")
        
        # Inspect admins
        if 'admins' in tables:
            output.append("\nAdmins:")
            cursor.execute("SELECT id, username, name, email, level FROM admins")
            for row in cursor.fetchall():
                output.append(f" - {row}")
        
        # Inspect staff
        if 'staff' in tables:
            output.append("\nStaff:")
            cursor.execute("SELECT id, staff_id, name, email, department FROM staff")
            for row in cursor.fetchall():
                output.append(f" - {row}")
        
        # Inspect finances
        if 'system_finances' in tables:
            output.append("\nSystem Finances:")
            cursor.execute("SELECT * FROM system_finances")
            for row in cursor.fetchall():
                output.append(f" - {row}")
        
        conn.close()
    except Exception as e:
        output.append(f"Error checking database: {e}")
    
    with open('db_results.txt', 'w') as f:
        f.write('\n'.join(output))
    print("Results written to db_results.txt")

if __name__ == "__main__":
    check_db()
