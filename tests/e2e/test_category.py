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
        """
        Test the creation of a new category.

        This test sends a POST request to the /api/v1/category endpoint with a JSON payload
        containing the name of the category to be created. It then asserts that the response
        status code is 200 and that the name of the created category in the response matches
        the name sent in the request.

        Assertions:
            - The response status code should be 200.
            - The name of the created category in the response should match the name sent in the request.
        """
        name_category_create = "category_test"
        response = self.client.post(
            "/api/v1/category",
            json={"name": name_category_create},
        )
        assert response.status_code == 200
        assert response.json()["data"]["name"] == name_category_create

    def test_get_categories(self):
        """
        Test the creation and retrieval of categories.

        This test performs the following steps:
        1. Creates 10 new categories by sending POST requests to the /api/v1/category endpoint.
        2. Verifies that each POST request returns a status code of 200.
        3. Retrieves the list of all categories by sending a GET request to the /api/v1/category endpoint.
        4. Verifies that the GET request returns a status code of 200.
        5. Asserts that the total number of categories retrieved is 11.

        The test assumes that there is already one category present before the test runs.
        """
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
        """
        Test the retrieval of a single category by its ID.

        This test performs the following steps:
        1. Creates a new category using a POST request to the /api/v1/category endpoint.
        2. Asserts that the response status code is 200 (OK).
        3. Extracts the category ID from the response.
        4. Retrieves the created category using a GET request to the /api/v1/category/{id} endpoint.
        5. Asserts that the response status code is 200 (OK).
        6. Asserts that the retrieved category ID matches the created category ID.
        """
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
        """
        Test case for retrieving a category with an invalid ID.

        This test sends a GET request to the endpoint for retrieving a category
        with an ID of 0, which is assumed to be invalid. It asserts that the
        response status code is 400 (Bad Request) and that the response JSON
        contains a message indicating that the category was not found.
        """
        response = self.client.get("/api/v1/category/0")
        assert response.status_code == 400
        assert response.json()["message"] == "Category not found"
