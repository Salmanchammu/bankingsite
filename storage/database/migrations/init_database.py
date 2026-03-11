#!/usr/bin/env python3
"""
Smart Bank - Database Initialization (Fixed)
Run from the database/ folder: python init_database.py
"""

import sqlite3
import os
import sys

DB_PATH = 'smart_bank.db'

def init_database():
    print("=" * 52)
    print("  Smart Bank - Database Initialization")
    print("=" * 52)

    # Always work from the script's own directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Remove old database silently so re-runs always work
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("  Removed old database")

    try:
        from werkzeug.security import generate_password_hash
    except ImportError:
        print("\n[ERROR] werkzeug not installed.")
        print("  Run:  pip install flask flask-cors werkzeug")
        sys.exit(1)

    print(f"\n  Creating: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # Path to the main schema file
    backend_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..', 'backend'))
    schema_path = os.path.join(backend_dir, 'schema.sql')
    
    if os.path.exists(schema_path):
        print(f"  Reading schema from: {schema_path}")
        with open(schema_path, 'r') as f:
            cur.executescript(f.read())
    else:
        print(f"  [ERROR] Schema file not found: {schema_path}")
        sys.exit(1)
    conn.commit()
    print("  [OK] All tables created")

    print("\n  Database is ready with empty tables")
    print("  Use the signup/registration features to create accounts")

    conn.close()

    print("\n" + "=" * 52)
    print("  DATABASE READY!")
    print("=" * 52)
    print("""
  FRESH DATABASE - NO SAMPLE DATA
  --------------------------------
  All tables have been created with no pre-existing data.
  
  To get started:
  1. Start the backend server
  2. Use the signup page to create accounts
  3. Or use the backend API to register users/staff/admin
  
  Database Location:
""")
    print(f"  {os.path.abspath(DB_PATH)}")
    print("=" * 52)
    print("  NEXT STEP:  cd ../backend && python app.py")
    print("=" * 52)

if __name__ == '__main__':
    init_database()
