"""Test main configuration for movie-recommender-backend-project"""
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)
