from flask_testing import TestCase
from flask import json
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2)

    def test_get_product_by_id(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        #print(product)
        self.assertEqual(product["name"], "Skello")

    def test_get_product_by_id_error_404(self):
        response = self.client.get("/api/v1/products/10")
        self.assertEqual(response.status, "404 NOT FOUND")

    def test_delete_product_by_id(self):
        response = self.client.delete("/api/v1/products/3")
        #print(response)
        self.assertEqual(response.status, "204 NO CONTENT")

    def test_create_new_product(self):
        response = self.client.post("/api/v1/products",
                                    data=json.dumps(dict(id=4, name='titi')),
                                    content_type="application/json")
        #print(response)
        self.assertEqual(response.status, "201 CREATED")

    def test_update_product_by_id(self):
        response = self.client.patch("/api/v1/products/3",
                                     data=json.dumps(dict(id=3, name='patch_toto')),
                                     content_type="application/json")
        print(response)
        self.assertEqual(response.status, "204 NO CONTENT")

    def test_update_product_by_id_empty(self):
        response = self.client.patch("/api/v1/products/3",
                                     data=json.dumps(dict(id=3, name='')),
                                     content_type="application/json")
        print(response)
        self.assertEqual(response.status, "422 UNPROCESSABLE ENTITY")
