from flask_testing import TestCase
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

