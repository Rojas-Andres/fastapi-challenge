import os
from starlette.testclient import TestClient
from unittest import TestCase
from tests.e2e.base_test import init_testing
from faker import Faker
import random


fake = Faker()


class TestReviews(TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DATABASE_NAME"] = "reviews_test"
        init_testing("reviews_test")

    def setUp(self):
        super().setUp()
        from app.main import app

        with TestClient(app) as client:
            self.client = client
        os.environ["DATABASE_NAME"] = "reviews_test"

    def test_create_review_location_not_found(self):
        response = self.client.post(
            "/api/v1/reviews",
            json={
                "location_id": 0,
                "category_id": 0,
            },
        )
        assert response.status_code == 400
        assert response.json()["message"] == "Location not found"

    def test_create_review_category_not_found(self):
        name_location_create = fake.name()
        response = self.client.post(
            "/api/v1/locations",
            json={
                "name": name_location_create,
                "latitude": 40.7128,
                "longitude": -74.006,
            },
        )
        assert response.status_code == 200
        assert response.json()["data"]["name"] == name_location_create
        location_id = response.json()["data"]["id"]
        response = self.client.post(
            "/api/v1/reviews",
            json={
                "location_id": location_id,
                "category_id": 0,
            },
        )
        assert response.status_code == 400
        assert response.json()["message"] == "Category not found"

    def test_create_review(self):
        name_location_create = fake.name()
        response = self.client.post(
            "/api/v1/locations",
            json={
                "name": name_location_create,
                "latitude": 40.7128,
                "longitude": -74.006,
            },
        )
        assert response.status_code == 200
        assert response.json()["data"]["name"] == name_location_create
        location_id = response.json()["data"]["id"]
        name_category_create = fake.name()
        response = self.client.post(
            "/api/v1/category",
            json={"name": name_category_create},
        )
        assert response.status_code == 200
        assert response.json()["data"]["name"] == name_category_create
        category_id = response.json()["data"]["id"]
        response = self.client.post(
            "/api/v1/reviews",
            json={
                "location_id": location_id,
                "category_id": category_id,
            },
        )
        assert response.status_code == 200
        assert response.json()["data"]["location_id"] == location_id
        assert response.json()["data"]["category_id"] == category_id
