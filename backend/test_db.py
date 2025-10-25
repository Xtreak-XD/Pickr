#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Setup Django
django.setup()

from django.db import connection

def test_database_connection():
    try:
        print("Testing database connection...")
        
        # Test basic connection
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        print(f"✓ Database connected successfully!")
        print(f"PostgreSQL version: {version}")
        
        # List all tables
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)
        
        tables = [row[0] for row in cursor.fetchall()]
        print(f"\n📋 Tables found in database ({len(tables)} total):")
        for table in tables:
            print(f"  - {table}")
            
        # Check if our app tables exist
        app_tables = [t for t in tables if any(t.startswith(prefix) for prefix in ['listings_', 'swipes_', 'users_'])]
        print(f"\n🎯 App-specific tables ({len(app_tables)} total):")
        for table in app_tables:
            print(f"  - {table}")
            
        if not app_tables:
            print("⚠️  No app-specific tables found! You may need to run migrations.")
        else:
            print("✓ App tables are present in the database!")
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False
        
    return True

if __name__ == "__main__":
    test_database_connection()