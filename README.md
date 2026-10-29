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
- Python
- scikit-learn
- FastAPI
- pytest
- Ruff
- Docker (pending setup)
- GitHub Actions (pending setup)

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
```

Example response:

```json
{
  "prediction": 0,
  "species": "setosa"
}
```

## Run Locally

Train the model:

```powershell
.\.venv\Scripts\python.exe src\train\train.py
```

Start the API:

```powershell
.\.venv\Scripts\python.exe -m uvicorn src.app.main:app --reload
```

Open the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Run Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

## Code Quality

```powershell
.\.venv\Scripts\python.exe -m ruff check src tests
```

## Project Status

- [x] Model training
- [x] FastAPI endpoints
- [x] Five automated tests
- [x] Ruff code-quality check
- [ ] Docker image build and scan
- [ ] GitHub Actions CI workflow
- [ ] Publish image to GitHub Container Registry
