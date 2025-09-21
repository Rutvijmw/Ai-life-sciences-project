# AI-Driven Drug Response Prediction & Knowledge Graph (Life Sciences)

[![Tests](https://img.shields.io/github/actions/workflow/status/USER/REPO/ci.yml?label=tests)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()

End-to-end portfolio project designed to match a **Data Scientist (Life Sciences, Scientific AI)** role.  
It demonstrates survival analysis, Bayesian modeling, transformers for literature evidence, and a biomedical **knowledge graph** with GNN-ready structure, plus an interactive **Streamlit dashboard**.

## ✨ Highlights
- Survival analysis (Kaplan–Meier, CoxPH) on synthetic drug response data.
- Bayesian modeling of treatment effects (PyMC).
- Literature evidence stub using HuggingFace transformers + LangChain.
- Knowledge Graph (NetworkX, Neo4j-ready) connecting drugs–targets–diseases.
- Clean OOP Python package under `src/` with tests.
- Streamlit dashboard for non-technical stakeholders.
- CI-ready GitHub Actions workflow.

> Swap in real datasets later (TCGA, ChEMBL, DrugBank, PubMed). This scaffold runs with synthetic data so you can demo immediately.

## 🧱 Project Structure
```
ai_life_sciences_project/
├─ data/
│  ├─ raw/                # place external data here
│  └─ processed/          # generated datasets
├─ notebooks/             # EDA and reports
├─ src/
│  ├─ kg/                 # knowledge graph builder & utilities
│  ├─ models/             # survival, bayesian, (GNN stub)
│  ├─ nlp/                # literature QA / embeddings
│  └─ utils/              # helpers (io, metrics)
├─ dashboard/             # Streamlit app
├─ tests/                 # unit tests
├─ scripts/               # CLI commands (train, evaluate, build KG)
└─ .github/workflows/     # CI
```

## 🚀 Quickstart
```bash
# 1) Create environment
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run smoke tests
pytest -q

# 4) Generate synthetic data & train demo models
python scripts/generate_data.py
python scripts/train_survival.py
python scripts/run_bayesian.py
python scripts/build_kg.py

# 5) Launch dashboard
streamlit run dashboard/app.py
```

## 📊 Dashboard
- Upload or select a patient cohort to view **survival curves**.
- Compare treatment arms with **hazard ratios** and credible intervals.
- Query the knowledge graph to see related **drugs → targets → diseases**.
- Search abstracts (stub) for recent literature.
# 🧬 AI-Driven Drug Response Prediction & Knowledge Graph (Life Sciences)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-brightgreen)](https://streamlit.io/)  
[![Tests](https://img.shields.io/badge/Tests-Passing-blue)](https://docs.pytest.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

End-to-end portfolio project designed to match a **Data Scientist (Life Sciences, Scientific AI)** role.  
It demonstrates **survival analysis, Bayesian modeling, transformers for literature evidence, and a biomedical knowledge graph** with GNN-ready structure — plus an interactive **Streamlit dashboard**.

---

## ✨ Highlights
- 📊 Survival analysis (Kaplan–Meier, CoxPH) on synthetic drug response data  
- 🔮 Bayesian modeling of treatment effects with PyMC  
- 📚 Literature evidence stub using HuggingFace transformers + LangChain  
- 🧩 Knowledge Graph (NetworkX, Neo4j-ready) connecting drugs–targets–diseases  
- 🧑‍💻 Clean OOP Python package under `src/` with tests  
- 🎛️ Streamlit dashboard for non-technical stakeholders  
- ⚙️ CI-ready GitHub Actions workflow  

> Swap in real datasets later (TCGA, ChEMBL, DrugBank, PubMed). This scaffold runs with synthetic data so you can demo immediately.

---

## 🧱 Project Structure

## 🧪 Tests
```bash
pytest -q

## 📌 Roadmap
- Replace synthetic with TCGA/ChEMBL/DrugBank datasets.
- Add GNN link prediction (PyTorch Geometric or DGL).
- Add causal inference (DoWhy/EconML) for treatment effect estimation.
- Containerize with Docker & deploy to cloud.

## ⚖️ License
MIT
# 🧬 AI-Driven Drug Response Prediction & Knowledge Graph (Life Sciences)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-brightgreen)](https://streamlit.io/)  
[![Tests](https://img.shields.io/badge/Tests-Passing-blue)](https://docs.pytest.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

End-to-end portfolio project designed to match a **Data Scientist (Life Sciences, Scientific AI)** role.  
It demonstrates **survival analysis, Bayesian modeling, transformers for literature evidence, and a biomedical knowledge graph** with GNN-ready structure — plus an interactive **Streamlit dashboard**.

---

## ✨ Highlights
- 📊 Survival analysis (Kaplan–Meier, CoxPH) on synthetic drug response data  
- 🔮 Bayesian modeling of treatment effects with PyMC  
- 📚 Literature evidence stub using HuggingFace transformers + LangChain  
- 🧩 Knowledge Graph (NetworkX, Neo4j-ready) connecting drugs–targets–diseases  
- 🧑‍💻 Clean OOP Python package under `src/` with tests  
- 🎛️ Streamlit dashboard for non-technical stakeholders  
- ⚙️ CI-ready GitHub Actions workflow  

> Swap in real datasets later (TCGA, ChEMBL, DrugBank, PubMed). This scaffold runs with synthetic data so you can demo immediately.

---

## 🧱 Project Structure
