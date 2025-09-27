import pandas as pd
from src.models.survival import SurvivalModel

def test_survival_smoke():
    # Minimal synthetic dataset (no files needed)
    df = pd.DataFrame({
        "time":      [6, 12, 8, 10, 7, 5],
        "event":     [1, 1, 0, 1, 1, 0],
        "age":       [55, 60, 50, 62, 47, 70],
        "treatment": [0, 1, 0, 1, 1, 0],
    })
    model = SurvivalModel()
    model.fit(df, covariates=["age","treatment"])
    # Just ensure model trained and summary is available
    assert model.summary() is not None
