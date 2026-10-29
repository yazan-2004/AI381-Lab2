from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "model.joblib"


def train():
    iris = load_iris()

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000, random_state=42)
    )

    model.fit(iris.data, iris.target)
    joblib.dump(model, MODEL_PATH)

    print("Model trained successfully!")
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Training samples: {len(iris.data)}")


if __name__ == "__main__":
    train()