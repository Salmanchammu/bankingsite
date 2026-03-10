"""
Migration: Create service_applications table
Used to track Mutual Fund, Life Insurance, Gold Loan, Fixed Deposit, and general Loan applications.
"""
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'smart_bank.db')


def migrate():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Check if table already exists
    existing = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='service_applications'"
    ).fetchone()

    if existing:
        print("service_applications table already exists. Skipping.")
        conn.close()
        return

    cursor.execute('''
        CREATE TABLE service_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            service_type TEXT NOT NULL,
            product_name TEXT,
            amount REAL,
            tenure INTEGER,
            account_id INTEGER,
            status TEXT DEFAULT 'pending',
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            processed_at TIMESTAMP,
            processed_by INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("service_applications table created successfully!")


if __name__ == '__main__':
    migrate()
