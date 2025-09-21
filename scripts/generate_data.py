"""Generate processed copies / small feature tables from raw data (synthetic)."""
from src.utils.io import load_csv, save_csv
import pandas as pd

def main():
    df = load_csv("raw/drug_response_synthetic.csv")
    # trivial feature engineering
    df["age_centered"] = (df["age"] - df["age"].mean())
    save_csv(df, "processed/drug_response_features.csv")
    print("Wrote data/processed/drug_response_features.csv")

if __name__ == "__main__":
    main()
