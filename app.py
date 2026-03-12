# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: Define mock data for a list of products
# Example: Each product should have id, name, price, and category
products = [
    {"id": 1, "name": "Wireless Headphones", "price": 79.99, "category": "Electronics"},
    {"id": 2, "name": "Running Shoes", "price": 120.00, "category": "Footwear"},
    {"id": 3, "name": "Coffee Maker", "price": 45.50, "category": "Kitchen"},
    {"id": 4, "name": "Yoga Mat", "price": 30.00, "category": "Fitness"},
    {"id": 5, "name": "Bluetooth Speaker", "price": 55.99, "category": "Electronics"},
    {"id": 6, "name": "Leather Wallet", "price": 25.00, "category": "Accessories"},
    {"id": 7, "name": "Stainless Water Bottle", "price": 18.99, "category": "Kitchen"},
    {"id": 8, "name": "Desk Lamp", "price": 34.00, "category": "Home Office"},
    {"id": 9, "name": "Sunglasses", "price": 89.99, "category": "Accessories"},
    {"id": 10, "name": "Jump Rope", "price": 12.50, "category": "Fitness"},
]

# TODO: Implement a homepage route that returns a JSON welcome message
@app.route("/")
def index():
    return jsonify({"message": "Welcome to Milkah's product catalog]", "resource endpoint": "/products"}), 200

# TODO: Implement GET /products to return all products or filter by category
@app.route("/products", methods=["GET"])
def fetch_products():
    category = request.args.get("category")
    if category: 
            categorized = [product for product in products if product["category"].lower() == category.lower()]
            if not categorized:
                 return "This category does not exist, please try again", 404
            return jsonify(categorized), 200
    else: 
        return jsonify(products), 200

# TODO: Implement GET /products/<id> to return a single product by ID
@app.route("/products/<int:id>", methods=["GET"])
def product_by_id(id):
    for product in products:
        if product["id"] == (id):
            return jsonify(product), 200
    return jsonify({"message":"No product with this id exists!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
