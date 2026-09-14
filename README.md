Django Inventory and Sales Management System

A Django-based inventory and sales management web application for managing products, suppliers, customers, orders, and stock movements.

The project demonstrates practical Django development, PostgreSQL integration, business logic, transactions, image uploads, and production deployment.

Live Demo

"View the Live Application" (https://django-inventory-sales-system-im1i.onrender.com/)

The live demo is currently hosted on Render's free tier, so it may take a short time to wake up after being inactive.

Features

Inventory Management

- Create and manage products
- Manage suppliers
- Track stock levels
- Record stock receipts
- Record stock sales
- Configure low-stock thresholds
- Upload product images
- Activate or deactivate products

Sales and Orders

- Browse available products
- View product details
- Add products to orders
- Create customer profiles
- Create customer orders
- Automatically calculate order totals
- Process payments
- Automatically deduct stock after payment
- Prevent sales when stock is insufficient

Business Logic

Stock operations are handled through dedicated service functions.

The payment workflow uses database transactions to ensure stock deductions and order status changes are handled safely.

Tech Stack

Technology| Purpose
Python| Programming language
Django| Web framework
PostgreSQL| Database
HTML5| Frontend structure
Django Templates| Server-side rendering
Tailwind CSS| UI styling
Gunicorn| Production application server
WhiteNoise| Static file serving
Pillow| Image processing
python-dotenv| Environment variables
dj-database-url| Database configuration

Project Structure

django-inventory-sales-system/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── inventory/
│   ├── models.py
│   ├── forms.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── sales/
│   ├── models.py
│   ├── forms.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/
│   └── base.html
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

Core Models

Inventory

Supplier

Stores:

- Name
- Email
- Phone

Product

Stores:

- Name
- SKU
- Cost price
- Selling price
- Low-stock threshold
- Description
- Supplier
- Product image
- Active status

StockMovement

Records:

- Product
- Movement type
- Quantity change
- Note

Stock is calculated from stock movements instead of manually storing a stock balance.

Sales

Customer

Stores:

- Name
- Phone
- Email
- Address

Order

Stores:

- Customer
- Order date
- Status

OrderItem

Stores:

- Order
- Product
- Quantity
- Unit price

Order totals are calculated from individual order items.

Installation and Setup

1. Clone the repository

Using HTTPS:

git clone https://github.com/sammyn7m-bit/django-inventory-sales-system.git

Enter the project directory:

cd django-inventory-sales-system

2. Create a virtual environment

python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a ".env" file in the project root:

SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=inventory_db
DB_USER=inventory_user
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=5432

Never commit your ".env" file or production secrets to GitHub.

5. Run database migrations

python manage.py migrate

6. Create an admin account

python manage.py createsuperuser

7. Start the development server

python manage.py runserver

Open the application at:

"http://127.0.0.1:8000/" (http://127.0.0.1:8000/)

Database

The application uses PostgreSQL.

Local development is configured using PostgreSQL environment variables, while production can use a PostgreSQL "DATABASE_URL".

The repository includes Django migrations, so after cloning the project you only need to run:

python manage.py migrate

Security

Sensitive configuration is stored using environment variables.

The following are excluded from Git:

.env
media/
staticfiles/
__pycache__/
*.pyc

Production Deployment

The application is configured for production deployment using:

- Gunicorn
- WhiteNoise
- PostgreSQL
- Environment variables
- Django production settings

Production start command:

gunicorn core.wsgi:application

Collect static files:

python manage.py collectstatic --noinput

What This Project Demonstrates

This project demonstrates practical experience with:

- Django models and relationships
- Class-based views
- Django forms
- CRUD operations
- PostgreSQL
- Service-layer business logic
- Database transactions
- Inventory management
- Order processing
- Payment workflows
- Image uploads
- Static file handling
- Environment-based configuration
- Production deployment

Future Improvements

- User authentication and roles
- Admin dashboard
- Sales and inventory statistics
- Multiple products per order
- Order history
- Sales reports
- Low-stock alerts
- Search and filtering
- Pagination
- Improved media storage

Author

Sammy Njuguna

Computer Science Student | Backend Developer

GitHub: "https://github.com/sammyn7m-bit" (https://github.com/sammyn7m-bit)

Project Repository: "https://github.com/sammyn7m-bit/django-inventory-sales-system" (https://github.com/sammyn7m-bit/django-inventory-sales-system)

Live Demo: "https://django-inventory-sales-system-im1i.onrender.com/" (https://django-inventory-sales-system-im1i.onrender.com/)
