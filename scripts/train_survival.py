"""Train survival model and export Cox summary to processed folder."""
from src.utils.io import load_csv, save_csv
from src.models.survival import SurvivalModel
import pandas as pd

def main():
    df = load_csv("processed/drug_response_features.csv")
    model = SurvivalModel()
    model.fit(df, covariates=["age","treatment"])
    summary = model.summary().reset_index().rename(columns={"index":"covariate"})
    save_csv(summary, "processed/cox_summary.csv")
    print("Wrote data/processed/cox_summary.csv")

if __name__ == "__main__":
    main()
