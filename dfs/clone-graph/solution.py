class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node | None") -> "Node | None":
        if node is None:
            return None

        visited: dict[Node, Node] = {}

        def dfs(original: Node) -> Node:
            if original in visited:
                return visited[original]
            clone = Node(original.val)
            visited[original] = clone
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)


def build_graph(adj_list: list[list[int]]) -> "Node | None":
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list, start=1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def to_adj_list(start: "Node | None") -> list[list[int]]:
    if start is None:
        return []
    visited: dict[int, Node] = {}
    stack = [start]
    while stack:
        n = stack.pop()
        if n.val in visited:
            continue
        visited[n.val] = n
        stack.extend(n.neighbors)
    return [sorted(neigh.val for neigh in visited[v].neighbors) for v in sorted(visited)]


if __name__ == "__main__":
    original_adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build_graph(original_adj)
    cloned = Solution().cloneGraph(original)

    assert cloned is not original
    assert to_adj_list(cloned) == original_adj

    # ensure clone is a fully separate object graph
    seen_ids = set()
    stack = [cloned]
    orig_ids = {id(n) for n in [original] + [nb for n in [original] for nb in n.neighbors]}
    while stack:
        n = stack.pop()
        if id(n) in seen_ids:
            continue
        seen_ids.add(id(n))
        assert id(n) not in orig_ids
        stack.extend(n.neighbors)

    # single node, no neighbors
    single = build_graph([[]])
    cloned_single = Solution().cloneGraph(single)
    assert cloned_single.val == 1
    assert cloned_single.neighbors == []
    assert cloned_single is not single

    # empty graph
    assert Solution().cloneGraph(None) is None

    print("ok")
