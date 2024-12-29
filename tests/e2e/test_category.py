import os
from starlette.testclient import TestClient
from unittest import TestCase
from tests.e2e.base_test import init_testing
from app.main import app


class TestCategory(TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DATABASE_NAME"] = "category_test"
        init_testing("category_test")

    def setUp(self):
        super().setUp()

        with TestClient(app) as client:
            self.client = client

    def test_create_category(self):
        name_category_create = "category_test"
        response = self.client.post(
            "/api/v1/category",
            json={"name": name_category_create},
        )
        assert response.status_code == 200
        # assert response.json()["data"]["name"] == name_category_create
