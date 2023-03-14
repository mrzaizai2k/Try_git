from http import HTTPStatus
from typing import Dict

# app/api.py
from fastapi import FastAPI

# Define application
app = FastAPI(
    title="TagIfAI - Made With ML",
    description="Classify machine learning projects.",
    version="0.1",
)


# app/api.py

@app.get("/")
def _index() -> Dict:
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {1243},
    }
    return response