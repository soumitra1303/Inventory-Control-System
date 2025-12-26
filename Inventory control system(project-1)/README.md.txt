# 📦 Inventory Control System

A complete web-based inventory management system built with Flask, featuring real-time stock tracking, low-stock alerts, and comprehensive reporting.

## ✨ Features

- ✅ **CRUD Operations**: Add, view, edit, and delete inventory items
- 📊 **Dashboard**: Real-time statistics and overview
- 🔍 **Search & Filter**: Find items by name, category
- 📈 **Reports**: Category-wise summaries, top items, low stock alerts
- ⚠️ **Low Stock Alerts**: Automatic notifications for items below minimum level
- 💰 **Value Tracking**: Calculate total inventory value
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🖨️ **Print Reports**: Generate printable inventory reports

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **No external dependencies** (except Flask)

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

### Step 1: Extract the Project

Extract all files maintaining the following structure:

```
inventory-control-system/
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── templates/
    ├── index.html
    ├── add_item.html
    ├── edit_item.html
    └── reports.html
```

### Step 2: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Verify installation:
   ```bash
   python --version
   ```

### Step 3: Install Dependencies

Open terminal/command prompt in the project folder:

```bash
# Install Flask
pip install -r requirements.txt
```

Or install directly:
```bash
pip install Flask==3.0.0
```

### Step 4: Initialize Database

```bash
python database.py
```

This will create `inventory.db` with sample data.

### Step 5: Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 6: Access the Application

Open your browser and go to:
```
http://localhost:5000
```

## 📖 Usage Guide

### Dashboard
- View all inventory items
- See real-time statistics (total items, quantity, value)
- Quick quantity updates
- Low stock alerts

### Adding Items
1. Click "Add Item" in navigation
2. Fill in all required fields:
   - Item Name
   - Category
   - Quantity
   - Unit Price
   - Supplier
   - Minimum Stock Level
3. Click "Save Item"

### Editing Items
1. Click the ✏️ (edit) icon on any item
2. Update the fields
3. Click "Update Item"

### Deleting Items
1. Click the 🗑️ (delete) icon
2. Confirm deletion

### Search & Filter
- Use the search box to find items by name
- Use category dropdown to filter by category
- Combine both for precise results

### Reports
- View category-wise summaries
- See top 10 items by value
- Check low stock items
- Print reports using the "Print Report" button

### Low Stock Alert
- Click "Low Stock Alert" button on dashboard
- See all items below minimum stock level
- Recommended reorder quantities shown

## 🔧 Configuration

### Change Port
Edit `app.py`, line at the bottom:
```python
app.run(debug=True, port=5000)  # Change 5000 to your desired port
```

### Modify Sample Data
Edit `database.py` and modify the `sample_data` list.

### Add Categories
Edit `templates/add_item.html` and `templates/edit_item.html`:
```html
<option value="YourCategory">YourCategory</option>
```

## 📊 Database Schema

### inventory table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| name | TEXT | Item name |
| category | TEXT | Item category |
| quantity | INTEGER | Current stock quantity |
| unit_price | REAL | Price per unit |
| supplier | TEXT | Supplier name |
| min_stock_level | INTEGER | Minimum stock threshold |
| description | TEXT | Item description |
| last_updated | TIMESTAMP | Last modification date |

## 🎯 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard |
| `/add` | GET, POST | Add new item |
| `/edit/<id>` | GET, POST | Edit item |
| `/delete/<id>` | POST | Delete item |
| `/search` | GET | Search items |
| `/low-stock` | GET | Get low stock items (JSON) |
| `/reports` | GET | Generate reports |
| `/update-quantity/<id>` | POST | Quick quantity update |
| `/api/categories` | GET | Get all categories (JSON) |

## 🐛 Troubleshooting

### "Flask is not recognized"
**Solution**: Install Flask
```bash
pip install Flask
```

### "Address already in use"
**Solution**: Change port in `app.py` or kill the process:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

### Database not found
**Solution**: Run database initialization
```bash
python database.py
```

### CSS not loading
**Solution**: Check folder structure. Ensure:
- `static/css/style.css` exists
- `static/js/main.js` exists
- Clear browser cache (Ctrl+F5)

### Port 5000 conflicts on Mac
**Solution**: Mac AirPlay uses port 5000. Either:
1. Disable AirPlay Receiver in System Preferences
2. Change port to 5001 or other

## 🔐 Security Notes

**For Production Deployment:**

1. Change the secret key in `app.py`:
   ```python
   app.config['SECRET_KEY'] = 'your-random-secure-key-here'
   ```

2. Set debug mode to False:
   ```python
   app.run(debug=False)
   ```

3. Use a production server (not Flask development server):
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

4. Add user authentication
5. Use PostgreSQL/MySQL instead of SQLite for production
6. Add input validation and sanitization
7. Implement HTTPS

## 📱 Features Walkthrough

### 1. Dashboard Statistics
- **Total Items**: Count of unique items in inventory
- **Total Quantity**: Sum of all item quantities
- **Total Value**: Sum of (quantity × unit_price) for all items
- **Low Stock Items**: Count of items at or below minimum stock level

### 2. Quick Quantity Update
- Directly edit quantity in the table
- Automatic calculation of total value
- Instant database update

### 3. Smart Search
- Real-time search as you type
- Searches in item name and description
- Case-insensitive matching

### 4. Category Filter
- Filter items by category
- Combine with search for precise results
- Dynamic category list from database

### 5. Low Stock Modal
- Popup showing all low stock items
- Calculates recommended reorder quantity
- Formula: (min_stock_level × 2) - current_quantity

### 6. Reports Page
- **Category Summary**: Total items, quantity, and value per category
- **Top 10 Items**: Highest value items
- **Low Stock Alert**: Items needing reorder
- Print-friendly layout

## 🎨 Customization

### Change Color Scheme
Edit `static/css/style.css`:
```css
/* Primary color (purple gradient) */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to blue gradient */
background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
```

### Modify Sample Data
Edit `database.py`, the `sample_data` list around line 30.

### Add New Fields
1. Modify database schema in `database.py`
2. Update forms in `add_item.html` and `edit_item.html`
3. Update table in `index.html`
4. Modify insert/update queries in `app.py`

## 📦 Sample Data Included

The system comes with 15 sample items across 4 categories:
- **Electronics**: Laptops, monitors, USB drives, etc.
- **Furniture**: Office chairs, desks, cabinets
- **Stationery**: Paper, pens, notebooks
- **Appliances**: Water dispensers, etc.

## 🚀 Future Enhancements

Potential features to add:
- [ ] User authentication and roles
- [ ] Barcode scanning
- [ ] Export to Excel/PDF
- [ ] Email notifications for low stock
- [ ] Purchase order management
- [ ] Sales tracking
- [ ] Multi-location support
- [ ] Mobile app (React Native/Flutter)
- [ ] Analytics dashboard with charts
- [ ] Batch operations (bulk update/delete)

## 📄 License

This project is open-source and available for educational purposes.

## 👨‍💻 Developer

Created for academic project submission.

**Roll Number**: 99  
**Project**: Inventory Control System (Non-AI Project 1)

## 🆘 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the error messages in terminal
3. Ensure all files are in correct locations
4. Verify Python and Flask versions

## 📝 Project Structure Explanation

```
inventory-control-system/
│
├── app.py                      # Main Flask application (routes, logic)
├── database.py                 # Database initialization and schema
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── static/                     # Static files (served directly)
│   ├── css/
│   │   └── style.css          # All styling
│   └── js/
│       └── main.js            # Frontend JavaScript (AJAX, events)
│
└── templates/                  # HTML templates (Jinja2)
    ├── index.html             # Main dashboard
    ├── add_item.html          # Add item form
    ├── edit_item.html         # Edit item form
    └── reports.html           # Reports page
```

## 🎓 Learning Outcomes

By working with this project, you'll learn:
- ✅ Full-stack web development
- ✅ Python Flask framework
- ✅ SQLite database operations
- ✅ RESTful API design
- ✅ CRUD operations
- ✅ Frontend-backend integration
- ✅ Responsive web design
- ✅ AJAX and asynchronous programming
- ✅ Data visualization and reporting

## ⚡ Quick Start Summary

```bash
# 1. Install Flask
pip install Flask

# 2. Initialize database
python database.py

# 3. Run application
python app.py

# 4. Open browser
http://localhost:5000
```

## 🎉 You're All Set!

Your Inventory Control System is now ready to use. Start by exploring the dashboard, add some items, and generate reports!

**Happy Inventory Management! 📦**