import streamlit as st
import pandas as pd
import plotly.express as px
from src.utils.io import load_csv
from src.models.survival import SurvivalModel

st.set_page_config(page_title="Drug Response & KG Dashboard", layout="wide")

st.title("AI-Driven Drug Response & Survival Analysis (Demo)")
st.write("Upload a cohort or use the synthetic dataset to explore survival curves and model summaries.")

opt = st.radio("Dataset", ["Synthetic (bundled)", "Upload CSV"], horizontal=True)
if opt == "Synthetic (bundled)":
    df = load_csv("raw/drug_response_synthetic.csv")
else:
    file = st.file_uploader("Upload CSV with columns: patient_id, age, treatment, time, event", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
    else:
        st.stop()

st.subheader("Preview")
st.dataframe(df.head())

model = SurvivalModel()
res = model.fit(df)

st.subheader("CoxPH Summary")
st.dataframe(model.summary())

st.subheader("Kaplan–Meier (Overall)")
km_df = pd.DataFrame({
    "timeline": res.km.survival_function_.index,
    "survival": res.km.survival_function_["Overall KM"].values
})
fig = px.line(km_df, x="timeline", y="survival", title="KM Survival Curve (Overall)")
st.plotly_chart(fig, use_container_width=True)

st.info("Knowledge Graph and Literature QA features are scaffolded in src/; swap in real data and models for production.")
