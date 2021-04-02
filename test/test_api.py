import unittest
import json
from api.app import app

class TestAPI(unittest.TestCase):
    # TODO: Find a better name for this test
    def test_api_ner_en_endpoint_can_load_en_model(self):
        with app.test_client() as client:
            res = client.get("/ner/en")
            data = res.get_data()
            assert data == b"Model loaded successfully"