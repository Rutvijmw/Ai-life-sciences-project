"""Build a tiny demo KG and export link table."""
from src.kg.graph_builder import KnowledgeGraph
from src.utils.io import save_csv

def main():
    kg = KnowledgeGraph()
    drugs = ["DrugA","DrugB"]
    targets = ["EGFR","BRAF"]
    diseases = ["CancerX","CancerY"]
    kg.add_entities(drugs, targets, diseases)
    kg.add_relations([("DrugA","targets","EGFR"), ("DrugB","targets","BRAF"), ("EGFR","implicated_in","CancerX")])
    links = kg.to_link_table()
    save_csv(links, "processed/kg_links.csv")
    print("Wrote data/processed/kg_links.csv")

if __name__ == "__main__":
    main()
