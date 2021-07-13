# How many edges in a complete graph on n nodes?
def make_edege(g, node_a, node_b):
    g[node_a].append((node_a, node_b))


def clique(n):
    graph = [[] for x in range(100)]

    # Create the graph
    for x in range(n):
        for y in range(x, n):
            if y > x:
                make_edege(graph, x, y + 1)

    edges = 0
    for x in graph:
        edges += len(x)

    return (edges)


for x in range(10):
    print(x, clique(x), (x * (x - 1)) // 2)
