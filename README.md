# AI381 Lab 2 — Iris Classifier

A machine learning API built with Python, scikit-learn, and FastAPI.

## Project Overview

This project trains a machine learning model to classify Iris flowers using four measurements:
- Sepal length
- Sepal width
- Petal length
- Petal width

The trained model is exposed through a REST API.

## Technologies

- Python 3.11
- scikit-learn
- FastAPI
- pytest
- Ruff
- Docker
- GitHub Actions
- Trivy
- GitHub Container Registry (GHCR)

## API Endpoints

### Health Check
`GET /health`

Returns the application health status.

### Prediction
`POST /predict`

Example request:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
