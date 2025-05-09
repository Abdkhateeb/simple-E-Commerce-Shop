# Muckie Backend

## Overview
Muckie Backend is a Django-based backend application designed to manage products. It provides an admin interface for managing product data and APIs for interacting with the product catalog.

## Features
- Product management with fields like name, description, price, and stock.
- Admin interface for managing products.
- API endpoints for product operations (to be implemented).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Muckie_Backend.git
   cd Muckie_Backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Project Structure
- `products/`: Contains the product-related models, views, serializers, and admin configurations.
- `project/`: Contains the main Django project settings and configurations.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
