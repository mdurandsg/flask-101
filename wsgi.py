from flask import Flask, jsonify, abort, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! I'm happy."

@app.route('/api/v1/products', methods=['GET', 'POST'])
def products():
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'toto'}
    ]
    if request.method == 'GET':
        return jsonify(PRODUCTS)
    else:
        result = request.get_json()
        PRODUCTS.append(result)
        return jsonify(PRODUCTS), 201

@app.route('/api/v1/products/<int:id>', methods=['GET', 'DELETE'])
def product_by_id(id):
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'toto'}
    ]
    index = id - 1
    if request.method == 'GET':
        if index <= len(PRODUCTS):
            return jsonify(PRODUCTS[index]), 200
        else:
            abort(404)
    else:
        del PRODUCTS[index]
        #print(PRODUCTS)
        return jsonify(""), 204
