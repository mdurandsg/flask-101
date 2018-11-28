from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! I'm happy."

@app.route('/api/v1/products')
def get_products():
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' }
    ]
    return jsonify(PRODUCTS)
