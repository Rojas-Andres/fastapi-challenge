import os
from unittest import TestCase

from faker import Faker
from starlette.testclient import TestClient

from tests.e2e.base_test import init_testing

fake = Faker()


class TestCategory(TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DATABASE_NAME"] = "category_test"
        init_testing("category_test")

    def setUp(self):
        super().setUp()
        from app.main import app

        with TestClient(app) as client:
            self.client = client
        os.environ["DATABASE_NAME"] = "category_test"

    def test_create_category(self):
        name_category_create = "category_test"
        response = self.client.post(
            "/api/v1/category",
            json={"name": name_category_create},
        )
        assert response.status_code == 200
        assert response.json()["data"]["name"] == name_category_create

    def test_get_categories(self):
        for _ in range(10):
            name_category_create = fake.name()
            response = self.client.post(
                "/api/v1/category",
                json={"name": name_category_create},
            )
            assert response.status_code == 200

        response = self.client.get("/api/v1/category")
        assert response.status_code == 200
        assert len(response.json()["data"]) == 11

    def test_get_only_category(self):
        response = self.client.post(
            "/api/v1/category",
            json={"name": fake.name()},
        )
        assert response.status_code == 200
        category_id = response.json()["data"]["id"]
        response = self.client.get("/api/v1/category/" + str(category_id))
        assert response.status_code == 200
        assert response.json()["data"]["id"] == category_id

    def test_category_id_not_found(self):
        response = self.client.get("/api/v1/category/0")
        assert response.status_code == 400
        assert response.json()["message"] == "Category not found"
