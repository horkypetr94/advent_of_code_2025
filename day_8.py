from itertools import combinations
import numpy as np
import networkx as nx
import pandas as pd

from loaders import load_list_from_lines
from tools import UnionFind


class ComponentTrackingUnionFind(UnionFind):
    def __init__(self, n):
        super().__init__(n)
        self.num_components = n
    def union(self, i, j):
        if super().union(i, j):
            self.num_components -= 1
            return True
        return False


def day_8_solution_1(clean_boxes):
    one = []
    two = []
    edge_weights = []
    for (i, box1), (j, box2) in combinations(enumerate(clean_boxes), 2):
        edge_weight = np.linalg.norm(box1 - box2)
        edge_weights.append(edge_weight)
        one.append(",".join(map(str, box1)))
        two.append(",".join(map(str, box2)))

    df = pd.DataFrame({"one": one, "two": two, "edge_weight": edge_weights})
    df.sort_values("edge_weight", ascending=True, inplace=True)

    limit = len(boxes)
    top_edges = df.iloc[:limit]

    G = nx.Graph()
    G.add_nodes_from(boxes)
    G.add_edges_from(zip(top_edges["one"], top_edges["two"]))

    sizes = sorted([len(c) for c in nx.connected_components(G)], reverse=True)
    print(sorted([c for c in nx.connected_components(G)]))
    answer = sizes[0] * sizes[1] * sizes[2]
    print(f"Top 3 sizes: {sizes[:3]}")
    print(f"Answer: {answer}")


def day_8_solution_2(clean_boxes):
    indices_i = []
    indices_j = []
    edge_weights = []

    for (i, box1), (j, box2) in combinations(enumerate(clean_boxes), 2):
        dist = np.linalg.norm(box1 - box2)
        indices_i.append(i)
        indices_j.append(j)
        edge_weights.append(dist)

    df = pd.DataFrame({"u": indices_i, "v": indices_j, "weight": edge_weights})
    df.sort_values("weight", ascending=True, inplace=True)

    uf = ComponentTrackingUnionFind(len(clean_boxes))

    for _, row in df.iterrows():
        u, v = int(row["u"]), int(row["v"])

        if uf.union(u, v):
            if uf.num_components == 1:
                box_u = clean_boxes[u]
                box_v = clean_boxes[v]

                x1 = box_u[0]
                x2 = box_v[0]

                print(f"Connected final pair: {box_u} and {box_v}")
                print(f"X coordinates: {x1} and {x2}")
                print(f"Answer: {x1 * x2}")
                return x1 * x2


boxes = load_list_from_lines("data/day_8_1")
clean_boxes = [np.array(list(map(int, box.split(",")))) for box in boxes]
day_8_solution_1(clean_boxes)
day_8_solution_2(clean_boxes)
