# Django Inventory and Sales Management System

A robust, Django-based inventory and sales management web application designed to track suppliers, monitor products, manage sales transactions, and automate stock calculations. 

## Features

- **Inventory Tracking:** Real-time monitoring of products, categories, and stock movement levels.
- **Sales & Ordering Flow:** Complete checkout pipeline linking customer orders to individual order items.
- **Stock Management Services:** Automated backend logic that adjusts inventory levels when sales are completed.
- **Supplier & Customer Management:** Dedicated models to track vendor sourcing and customer profiles.

##  Tech Stack

- **Backend:** Python, Django Web Framework
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** HTML5, CSS3, Django Templates

## Core Architecture & Models

Based on the development log, the repository structures data through these core modules:
- **Inventory:** Tracks `Product`, `Category`, and stock adjustments.
- **Sales & Orders:** Tracks `Customer`, `Order`, and individual `OrderItem` line items.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd django-inventory-sales-system
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   *(Ensure you create a requirements.txt file or list dependencies here)*
   ```bash
   pip install django
   ```

4. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0` in your browser to view the application.

