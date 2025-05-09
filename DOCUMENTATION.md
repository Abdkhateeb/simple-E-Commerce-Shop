# Documentation for Muckie Backend

## Models

### Product
The `Product` model represents a product in the catalog. It includes the following fields:
- `name`: A `CharField` for the product name (max length: 100).
- `short_description`: A `TextField` for a brief description (max length: 300).
- `product_description`: A `TextField` for a detailed description (max length: 5000).
- `price`: A `DecimalField` for the product price (max digits: 10, decimal places: 2).
- `stock`: A `SmallIntegerField` for the stock quantity (default: 0).

### Admin Configuration
The `ProductAdmin` class customizes the admin interface for the `Product` model:
- `list_display`: Displays `name`, `price`, and `stock` in the admin list view.
- `search_fields`: Allows searching by `name`.
- `list_filter`: Adds a filter for `stock`.
- `ordering`: Orders products by `-price` (descending).
- `list_per_page`: Limits the number of products displayed per page to 10.

## Setup and Usage

### Installation
Refer to the [README.md](README.md) for installation instructions.

### Running the Server
After setting up the project, run the development server using:
```bash
python manage.py runserver
```

### Admin Interface
Access the admin interface at `http://127.0.0.1:8000/admin/` to manage products.

## Future Enhancements
- Add API endpoints for CRUD operations on products.
- Implement user authentication and permissions.
- Add unit tests for models and views.
