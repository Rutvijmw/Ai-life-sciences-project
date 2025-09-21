from dataclasses import dataclass
import pandas as pd
from lifelines import KaplanMeierFitter, CoxPHFitter

@dataclass
class SurvivalResult:
    km: KaplanMeierFitter
    cox: CoxPHFitter

class SurvivalModel:
    def __init__(self, duration_col: str = "time", event_col: str = "event"):
        self.duration_col = duration_col
        self.event_col = event_col
        self.km = KaplanMeierFitter()
        self.cox = CoxPHFitter()

    def fit(self, df: pd.DataFrame, covariates: list[str] = ["age","treatment"]) -> SurvivalResult:
        # Kaplan–Meier by treatment (for plotting)
        self.km.fit(df[self.duration_col], event_observed=df[self.event_col], label="Overall KM")
        # Cox proportional hazards
        cox_df = df[[self.duration_col, self.event_col] + covariates].copy()
        self.cox.fit(cox_df, duration_col=self.duration_col, event_col=self.event_col)
        return SurvivalResult(self.km, self.cox)

    def predict_partial_hazard(self, df: pd.DataFrame) -> pd.Series:
        return self.cox.predict_partial_hazard(df)

    def summary(self) -> pd.DataFrame:
        return self.cox.summary
