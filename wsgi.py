from flask import Flask, jsonify, abort
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! I'm happy."

@app.route('/api/v1/products')
def get_products():
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'toto'}
    ]
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>')
def get_product_by_id(id):
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'toto'}
    ]
    index = id - 1
    if index <= len(PRODUCTS):
        return jsonify(PRODUCTS[index]), 200
    else:
        abort(404)
