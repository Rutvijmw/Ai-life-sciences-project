from dataclasses import dataclass
import networkx as nx
from typing import List, Tuple

@dataclass
class KGConfig:
    directed: bool = True

class KnowledgeGraph:
    def __init__(self, config: KGConfig = KGConfig()):
        self.G = nx.DiGraph() if config.directed else nx.Graph()

    def add_entities(self, drugs: list, targets: list, diseases: list):
        for d in drugs:
            self.G.add_node(d, type="drug")
        for t in targets:
            self.G.add_node(t, type="target")
        for dis in diseases:
            self.G.add_node(dis, type="disease")

    def add_relations(self, relations: List[Tuple[str, str, str]]):
        """relations: list of (src, relation, dst)"""
        for src, rel, dst in relations:
            self.G.add_edge(src, dst, relation=rel)

    def neighbors_of(self, node: str):
        return list(self.G.neighbors(node))

    def to_link_table(self):
        rows = []
        for u, v, data in self.G.edges(data=True):
            rows.append({"src": u, "relation": data.get("relation","related_to"), "dst": v})
        import pandas as pd
        return pd.DataFrame(rows)
