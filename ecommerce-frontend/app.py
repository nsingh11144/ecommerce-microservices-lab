from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # renders templates/index.html

@app.route('/products')
def products():
    return render_template('products.html')  # renders templates/products.html

@app.route('/cart')
def cart():
    return render_template('cart.html')  # renders templates/cart.html

if __name__ == '__main__':
    app.run(debug=True)
