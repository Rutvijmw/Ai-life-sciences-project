from src.models.survival import SurvivalModel
from src.utils.io import load_csv

def test_survival_smoke():
    df = load_csv("raw/drug_response_synthetic.csv")
    model = SurvivalModel()
    res = model.fit(df)
    assert res.km is not None
    assert model.summary() is not None
