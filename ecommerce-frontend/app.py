from flask import Flask, render_template
import requests

app = Flask(__name__)

PRODUCT_SERVICE_URL = "http://127.0.0.1:5001"  # Product Service runs on port 5001

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    # Fetch product list from Product Service
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    products_data = response.json()  # List of products
    return render_template('products.html', products=products_data)

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Frontend runs on 5000
