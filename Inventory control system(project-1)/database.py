import sqlite3
from datetime import datetime

DATABASE = 'inventory.db'

def get_db_connection():
    """Create database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with tables and sample data"""
    conn = get_db_connection()
    
    # Create inventory table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            supplier TEXT,
            min_stock_level INTEGER DEFAULT 10,
            description TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Check if table is empty and add sample data
    count = conn.execute('SELECT COUNT(*) FROM inventory').fetchone()[0]
    
    if count == 0:
        sample_data = [
            ('Laptop Dell XPS 15', 'Electronics', 15, 85000.00, 'Dell India', 5, 'High-performance laptop for office use'),
            ('Wireless Mouse', 'Electronics', 50, 500.00, 'Logitech', 20, 'Ergonomic wireless mouse'),
            ('Office Chair', 'Furniture', 25, 5500.00, 'Featherlite', 5, 'Ergonomic office chair with lumbar support'),
            ('A4 Paper Ream', 'Stationery', 100, 250.00, 'JK Paper', 30, '500 sheets per ream'),
            ('Whiteboard Marker', 'Stationery', 75, 50.00, 'Camlin', 25, 'Assorted colors'),
            ('USB Flash Drive 32GB', 'Electronics', 40, 450.00, 'SanDisk', 15, 'High-speed USB 3.0'),
            ('Desktop Computer', 'Electronics', 10, 45000.00, 'HP', 3, 'Intel i5, 8GB RAM, 512GB SSD'),
            ('Conference Table', 'Furniture', 5, 25000.00, 'Godrej', 2, 'Large conference table for 10 people'),
            ('Printer Ink Cartridge', 'Electronics', 30, 1200.00, 'Canon', 10, 'Black ink cartridge'),
            ('File Cabinet', 'Furniture', 8, 8500.00, 'Godrej', 3, '4-drawer steel file cabinet'),
            ('Notebook A5', 'Stationery', 200, 60.00, 'Classmate', 50, '200 pages ruled notebook'),
            ('Stapler', 'Stationery', 35, 150.00, 'Kangaro', 15, 'Heavy-duty stapler'),
            ('LED Monitor 24"', 'Electronics', 20, 12000.00, 'LG', 5, 'Full HD LED monitor'),
            ('Keyboard', 'Electronics', 30, 800.00, 'Logitech', 10, 'Wired USB keyboard'),
            ('Water Dispenser', 'Appliances', 3, 15000.00, 'Blue Star', 1, 'Hot and cold water dispenser')
        ]
        
        conn.executemany('''
            INSERT INTO inventory (name, category, quantity, unit_price, supplier, 
                                  min_stock_level, description, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', [(item[0], item[1], item[2], item[3], item[4], item[5], item[6], 
               datetime.now()) for item in sample_data])
        
        conn.commit()
        print("Database initialized with sample data!")
    
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database setup complete!")