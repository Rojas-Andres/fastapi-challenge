import os
import random
from unittest import TestCase

from faker import Faker
from starlette.testclient import TestClient

from tests.e2e.base_test import init_testing

fake = Faker()


class TestLocations(TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DATABASE_NAME"] = "location_test"
        init_testing("location_test")

    def setUp(self):
        super().setUp()
        from app.main import app

        with TestClient(app) as client:
            self.client = client
        os.environ["DATABASE_NAME"] = "location_test"

    def test_create_location(self):
        name_location_create = "location_test"
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

    def test_get_locations(self):
        for _ in range(10):
            name_location_create = fake.name()
            random_latitud = random.uniform(5.5, 10.5)
            random_lon = random.uniform(5.5, 10.5)
            response = self.client.post(
                "/api/v1/locations",
                json={
                    "name": name_location_create,
                    "latitude": random_latitud,
                    "longitude": random_lon,
                },
            )
            assert response.status_code == 200

        response = self.client.get("/api/v1/locations")
        assert response.status_code == 200
        assert len(response.json()["data"]) == 11

    def test_get_only_latitud(self):
        random_latitud = random.uniform(5.5, 10.5)
        random_lon = random.uniform(5.5, 10.5)
        response = self.client.post(
            "/api/v1/locations",
            json={
                "name": fake.name(),
                "latitude": random_latitud,
                "longitude": random_lon,
            },
        )
        assert response.status_code == 200
        location_id = response.json()["data"]["id"]
        response = self.client.get("/api/v1/locations/" + str(location_id))
        assert response.status_code == 200
        assert response.json()["data"]["id"] == location_id

    def test_location_id_not_found(self):
        response = self.client.get("/api/v1/locations/0")
        assert response.status_code == 400
        assert response.json()["message"] == "Location not found"
