from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import init_db, get_db_connection
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize database on first run
init_db()

@app.route('/')
def index():
    """Main dashboard - display all inventory items"""
    conn = get_db_connection()
    items = conn.execute('''
        SELECT * FROM inventory 
        ORDER BY id DESC
    ''').fetchall()
    conn.close()
    
    # Calculate statistics
    conn = get_db_connection()
    stats = conn.execute('''
        SELECT 
            COUNT(*) as total_items,
            SUM(quantity) as total_quantity,
            SUM(quantity * unit_price) as total_value,
            COUNT(CASE WHEN quantity <= min_stock_level THEN 1 END) as low_stock_count
        FROM inventory
    ''').fetchone()
    conn.close()
    
    return render_template('index.html', items=items, stats=stats)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    """Add new inventory item"""
    if request.method == 'POST':
        try:
            name = request.form['name']
            category = request.form['category']
            quantity = int(request.form['quantity'])
            unit_price = float(request.form['unit_price'])
            supplier = request.form['supplier']
            min_stock_level = int(request.form['min_stock_level'])
            description = request.form.get('description', '')
            
            conn = get_db_connection()
            conn.execute('''
                INSERT INTO inventory (name, category, quantity, unit_price, supplier, 
                                      min_stock_level, description, last_updated)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, category, quantity, unit_price, supplier, min_stock_level, 
                  description, datetime.now()))
            conn.commit()
            conn.close()
            
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {str(e)}", 400
    
    return render_template('add_item.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    """Edit existing inventory item"""
    conn = get_db_connection()
    
    if request.method == 'POST':
        try:
            name = request.form['name']
            category = request.form['category']
            quantity = int(request.form['quantity'])
            unit_price = float(request.form['unit_price'])
            supplier = request.form['supplier']
            min_stock_level = int(request.form['min_stock_level'])
            description = request.form.get('description', '')
            
            conn.execute('''
                UPDATE inventory 
                SET name=?, category=?, quantity=?, unit_price=?, supplier=?, 
                    min_stock_level=?, description=?, last_updated=?
                WHERE id=?
            ''', (name, category, quantity, unit_price, supplier, min_stock_level, 
                  description, datetime.now(), id))
            conn.commit()
            conn.close()
            
            return redirect(url_for('index'))
        except Exception as e:
            conn.close()
            return f"Error: {str(e)}", 400
    
    item = conn.execute('SELECT * FROM inventory WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if item is None:
        return "Item not found", 404
    
    return render_template('edit_item.html', item=item)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    """Delete inventory item"""
    try:
        conn = get_db_connection()
        conn.execute('DELETE FROM inventory WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/search')
def search():
    """Search inventory items"""
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    
    conn = get_db_connection()
    
    if category:
        items = conn.execute('''
            SELECT * FROM inventory 
            WHERE category = ? AND (name LIKE ? OR description LIKE ?)
            ORDER BY name
        ''', (category, f'%{query}%', f'%{query}%')).fetchall()
    else:
        items = conn.execute('''
            SELECT * FROM inventory 
            WHERE name LIKE ? OR description LIKE ? OR category LIKE ?
            ORDER BY name
        ''', (f'%{query}%', f'%{query}%', f'%{query}%')).fetchall()
    
    conn.close()
    
    return jsonify([dict(item) for item in items])

@app.route('/low-stock')
def low_stock():
    """Get items with low stock"""
    conn = get_db_connection()
    items = conn.execute('''
        SELECT * FROM inventory 
        WHERE quantity <= min_stock_level
        ORDER BY quantity ASC
    ''').fetchall()
    conn.close()
    
    return jsonify([dict(item) for item in items])

@app.route('/reports')
def reports():
    """Generate reports"""
    conn = get_db_connection()
    
    # Category-wise summary
    category_summary = conn.execute('''
        SELECT 
            category,
            COUNT(*) as item_count,
            SUM(quantity) as total_quantity,
            SUM(quantity * unit_price) as total_value
        FROM inventory
        GROUP BY category
        ORDER BY total_value DESC
    ''').fetchall()
    
    # Top items by value
    top_items = conn.execute('''
        SELECT 
            name,
            category,
            quantity,
            unit_price,
            (quantity * unit_price) as total_value
        FROM inventory
        ORDER BY total_value DESC
        LIMIT 10
    ''').fetchall()
    
    # Low stock items
    low_stock_items = conn.execute('''
        SELECT * FROM inventory 
        WHERE quantity <= min_stock_level
        ORDER BY quantity ASC
    ''').fetchall()
    
    conn.close()
    
    return render_template('reports.html', 
                         category_summary=category_summary,
                         top_items=top_items,
                         low_stock_items=low_stock_items)

@app.route('/update-quantity/<int:id>', methods=['POST'])
def update_quantity(id):
    """Quick update quantity"""
    try:
        data = request.get_json()
        new_quantity = int(data['quantity'])
        
        conn = get_db_connection()
        conn.execute('''
            UPDATE inventory 
            SET quantity = ?, last_updated = ?
            WHERE id = ?
        ''', (new_quantity, datetime.now(), id))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/categories')
def get_categories():
    """Get all unique categories"""
    conn = get_db_connection()
    categories = conn.execute('''
        SELECT DISTINCT category FROM inventory ORDER BY category
    ''').fetchall()
    conn.close()
    
    return jsonify([cat['category'] for cat in categories])

if __name__ == '__main__':
    app.run(debug=True, port=5000)