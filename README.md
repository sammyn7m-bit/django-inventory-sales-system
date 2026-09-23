# Django Inventory and Sales Management System

A robust, enterprise-ready Django-based inventory and sales management web application designed to track products, suppliers, customers, orders, and stock movements seamlessly. This project highlights practical Django development workflows, rigorous transaction management, and automated stock safety business logic.

Live Demo: https://django-inventory-sales-system-im1i.onrender.com
(Hosted on Render's free tier. Please allow a few moments for the server to spin up if it has been inactive.)

---

## Features

### Inventory Management
* **Dynamic Product Profiles:** Create, update, and manage products with structural parameters like SKUs, cost versus selling prices, and active/inactive toggle states.
* **Supplier Tracking:** Associate detailed supplier information with relevant product catalogs.
* **Intelligent Stock Control:** Set up custom low-stock thresholds and upload high-resolution product images.
* **Movement-Based Ledger:** Calculate live stock balances historically using dynamic receipts and sales records rather than manual overrides.

### Sales and Orders
* **Customer Hub:** Dedicated customer profiles tracking contact details and historical activity.
* **Transaction Engine:** Browse products, build client orders, and let the backend automatically compute precise totals.
* **Safe Checkouts:** Database transactions guarantee that stock deductions only process when a payment clears, preventing negative stock states.

---

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **Django** | Robust backend web framework |
| **PostgreSQL** | Relational database engine |
| **Tailwind CSS** | Clean, modern UI styling |
| **Gunicorn** | WSGI HTTP production server |
| **WhiteNoise** | High-efficiency static file serving |
| **Pillow** | Image processing utility |

---

## Project Structure

```text
django-inventory-sales-system/
│
├── core/                  # Project configuration directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── inventory/             # Inventory engine application
│   ├── models.py          # Supplier, Product, StockMovement
│   ├── services.py        # Dedicated stock operational functions
│   ├── views.py
│   └── urls.py
│
├── sales/                 # Customer and billing application
│   ├── models.py          # Customer, Order, OrderItem
│   ├── services.py        # Safe payment workflow processing
│   ├── views.py
│   └── urls.py
│
├── templates/             # Global HTML layouts & structural base
│   └── base.html
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Core Data Models

### Inventory Domain
* **Supplier:** Name, Email, Phone
* **Product:** Name, SKU, Cost Price, Selling Price, Low-Stock Threshold, Description, Supplier, Product Image, Active Status
* **StockMovement:** Product, Movement Type (Receipt/Sale), Quantity Change, Note

### Sales Domain
* **Customer:** Name, Phone, Email, Address
* **Order:** Customer, Order Date, Status
* **OrderItem:** Order, Product, Quantity, Unit Price

---

## Installation and Setup

### 1. Clone and Enter Repository
```bash
git clone https://github.com
cd django-inventory-sales-system
```

### 2. Configure Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root directory:
```env
SECRET_KEY=your-fallback-secret-key-here
DEBUG=True
DB_NAME=inventory_db
DB_USER=inventory_user
DB_PASSWORD=your-secure-password
DB_HOST=127.0.0.1
DB_PORT=5432
```
> Warning: The `.env` file containing local configurations and production secrets is ignored by Git and should never be committed to source control.

### 5. Initialize the Database
```bash
python manage.py migrate
```

### 6. Administrative Setup and Launch
```bash
# Create an admin user account
python manage.py createsuperuser

# Boot up the local runtime environment
python manage.py runserver
```
Visit the local server in your browser at: `http://127.0.0`

---

## Production Deployment

The project is pre-configured out-of-the-box for cloud hosting using:
* **Gunicorn** to process application tasks concurrently.
* **WhiteNoise** to serve production assets directly from Django.
* **Environment-level separation** utilizing `DATABASE_URL` connections.

### Key Deployment Tasks
```bash
# Static asset compilation
python manage.py collectstatic --noinput

# Production runtime entry point
gunicorn core.wsgi:application
```

---

## Future Improvements
* [ ] Role-Based Access Control (RBAC) and user authentication profiles.
* [ ] Multi-product cart optimizations per single order checkout.
* [ ] Rich analytics dashboard featuring real-time sales curves and inventory velocity graphs.
* [ ] Low-stock automated email or SMS notifications.
* [ ] Advanced server-side search querying, filtering, and pagination.

---

## Author

**Sammy Njuguna**  
*Computer Science Student and Backend Developer*

* **GitHub:** [@sammyn7m-bit](https://github.com)
* **Project Link:** [django-inventory-sales-system](https://github.com/sammyn7m-bit/django-inventory-sales-system)

