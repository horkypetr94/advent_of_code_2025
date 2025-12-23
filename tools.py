from collections import defaultdict


def remap_lol_values(lol, mapping):
    return [[mapping[c] for c in row] for row in lol]


def pad_lol_with_zeros(lol, pad=1):
    rows, cols = len(lol), len(lol[0])
    padded = [[0] * (cols + 2 * pad)]
    padded += [[0] * pad + row + [0] * pad for row in lol]
    padded += [[0] * (cols + 2 * pad)]
    return padded


moore_neighbourhood_dict = {
    "NW": (-1, -1),
    "N": (-1, 0),
    "NE": (-1, 1),
    "W": (0, -1),
    "E": (0, 1),
    "SW": (1, -1),
    "S": (1, 0),
    "SE": (1, 1),
}


def get_moore_neighbourhood(array, line, item):
    items = []
    for diff in moore_neighbourhood_dict.values():
        items.append(array[line + diff[0]][item + diff[1]])
    return items


class UnionFind:
    """
    A base Union-Find (Disjoint Set Union) implementation
    with Path Compression and Union by Rank optimizations.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Height of the tree to optimize union operations

    def find(self, i):
        """Finds the representative of the set containing i with path compression."""
        if self.parent[i] != i:
            # Path compression: Point node directly to the root
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Unites the sets containing i and j.
        Returns True if a merge happened, False if they were already united.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by Rank: Attach smaller tree to larger tree
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True  # Merge successful

        return False  # Already in the same set


def reverse_lookup(original_dict: dict) -> dict:
    """
    Constructs a reverse adjacency list (reverse index) from a given dictionary.

    This function inverts a "one-to-many" mapping. Where the input maps a
    source node to a list of destination nodes (Key -> [Value1, Value2]),
    this function maps each destination node back to the list of source nodes
    that point to it (Value1 -> [Key, ...]).

    This is essential for optimizing "who points to X?" queries, reducing
    the complexity from O(N) (scanning the whole dict) to O(1) (direct lookup).

    Args:
        original_dict (dict): A dictionary where keys are strings (source nodes)
            and values are lists of strings (destination nodes).
            Example: {'key1': ['val_a', 'val_b'], 'key2': ['val_a']}

    Returns:
        defaultdict(list): A dictionary where keys are the values from the
            original dictionary, and values are lists of keys that referenced them.
            Example: {'val_a': ['key1', 'key2'], 'val_b': ['key1']}
    """
    reverse_map = defaultdict(list)
    for key, values in original_dict.items():
        for val in values:
            reverse_map[val].append(key)
    return reverse_map
