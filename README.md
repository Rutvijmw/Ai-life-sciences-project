# 🧬 AI-Driven Drug Response Prediction & Knowledge Graph (Life Sciences)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-brightgreen)](https://streamlit.io/)  
[![Tests](https://github.com/Rutvijmw/Ai-life-sciences-project/actions/workflows/ci.yml/badge.svg)](https://github.com/Rutvijmw/Ai-life-sciences-project/actions/workflows/ci.yml)
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
ai_life_sciences_project/
├─ data/ # raw + processed datasets
├─ notebooks/ # exploratory analysis
├─ src/ # survival, bayesian, KG, NLP, utils
├─ dashboard/ # Streamlit app
├─ scripts/ # CLI pipeline scripts
├─ tests/ # unit tests
└─ .github/workflows/ # CI
