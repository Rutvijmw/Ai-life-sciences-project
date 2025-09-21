from dataclasses import dataclass
import pymc as pm
import arviz as az
import numpy as np
import pandas as pd

@dataclass
class BayesianResult:
    idata: az.InferenceData

class BayesianTreatmentEffect:
    """Simple Bayesian model: outcome ~ Normal(mu, sigma), mu = a + b * treatment + c * age"""
    def __init__(self, draws: int = 1000, chains: int = 2, tune: int = 1000, random_seed: int = 42):
        self.draws = draws
        self.chains = chains
        self.tune = tune
        self.random_seed = random_seed
        self.idata = None

    def fit(self, df: pd.DataFrame) -> BayesianResult:
        y = df["time"].values.astype(float)  # proxy outcome; replace with continuous endpoint if available
        trt = df["treatment"].values.astype(int)
        age = df["age"].values.astype(float)

        with pm.Model() as model:
            a = pm.Normal("a", 0, 10)
            b = pm.Normal("b", 0, 5)  # treatment effect
            c = pm.Normal("c", 0, 1)  # age slope
            sigma = pm.HalfNormal("sigma", 5)

            mu = a + b * trt + c * (age - age.mean())/age.std()

            y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)

            self.idata = pm.sample(draws=self.draws, chains=self.chains, tune=self.tune, random_seed=self.random_seed, progressbar=False)

        return BayesianResult(self.idata)

    def trt_effect_summary(self) -> pd.DataFrame:
        if self.idata is None:
            raise RuntimeError("Model not fit yet")
        return az.summary(self.idata, var_names=["b"])
