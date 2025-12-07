from flask import Flask, render_template
import requests

app = Flask(__name__)

# Use Kubernetes service FQDN
PRODUCT_SERVICE_URL = "http://product-service.backend.svc.cluster.local:5001"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    products_data = response.json()
    return render_template('products.html', products=products_data)

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)