# scripts/generate_data.py
# Create synthetic raw data AND a simple processed feature table
import pandas as pd
from src.utils.io import save_csv

def main():
    # Synthetic cohort
    df = pd.DataFrame({
        "patient_id": range(1, 31),
        "age": [55,60,62,45,50,70,66,53,59,61,58,64,52,49,47,68,73,65,56,62,51,54,57,60,63,66,69,71,74,48],
        "treatment": [0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0],
        "time": [6,12,10,8,14,5,13,7,11,9,6,12,8,7,13,5,10,12,7,11,6,10,8,12,7,11,5,13,12,7],
        "event": [1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0,1]
    })

    # Save RAW dataset into data/raw/
    save_csv(df, "raw/drug_response_synthetic.csv")

    # Simple processed features (example: centered age)
    feat = df.copy()
    feat["age_centered"] = feat["age"] - feat["age"].mean()

    # Save PROCESSED dataset into data/processed/
    save_csv(feat, "processed/drug_response_features.csv")

    print("Wrote data/raw/drug_response_synthetic.csv")
    print("Wrote data/processed/drug_response_features.csv")

if __name__ == "__main__":
    main()

