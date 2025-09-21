"""Run simple Bayesian model to estimate treatment effect."""
from src.utils.io import load_csv, save_csv
from src.models.bayesian import BayesianTreatmentEffect

def main():
    df = load_csv("processed/drug_response_features.csv")
    bayes = BayesianTreatmentEffect(draws=500, chains=2, tune=500)
    bayes.fit(df)
    eff = bayes.trt_effect_summary()
    save_csv(eff, "processed/bayesian_trt_effect.csv")
    print("Wrote data/processed/bayesian_trt_effect.csv")

if __name__ == "__main__":
    main()
