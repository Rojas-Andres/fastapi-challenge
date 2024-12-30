import os
import random
from unittest import TestCase

from faker import Faker
from starlette.testclient import TestClient

from tests.e2e.base_test import init_testing

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
        """
        Test case for creating a review when the specified location is not found.

        This test sends a POST request to the /api/v1/reviews endpoint with a
        non-existent location_id and category_id. It asserts that the response
        status code is 400 and the response message indicates that the location
        was not found.
        """
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
        """
        Test case for creating a review with a non-existent category.

        This test performs the following steps:
        1. Creates a new location using a POST request to the /api/v1/locations endpoint.
        2. Verifies that the location creation was successful and retrieves the location ID.
        3. Attempts to create a review for the newly created location with a category ID that does not exist (category_id=0).
        4. Asserts that the response status code is 400 (Bad Request).
        5. Asserts that the response message indicates that the category was not found.

        The test ensures that the API correctly handles the case where a review is created with an invalid category ID.
        """
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
        """
        Test the creation of a review.

        This test performs the following steps:
        1. Creates a new location with a random name and fixed latitude and longitude.
        2. Asserts that the location creation was successful and retrieves the location ID.
        3. Creates a new category with a random name.
        4. Asserts that the category creation was successful and retrieves the category ID.
        5. Creates a new review using the previously created location ID and category ID.
        6. Asserts that the review creation was successful and verifies the location ID and category ID in the response.

        Assertions:
        - The status code of the location creation response is 200.
        - The name of the created location matches the expected name.
        - The status code of the category creation response is 200.
        - The name of the created category matches the expected name.
        - The status code of the review creation response is 200.
        - The location ID in the review creation response matches the expected location ID.
        - The category ID in the review creation response matches the expected category ID.
        """
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
