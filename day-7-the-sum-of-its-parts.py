from collections import namedtuple
from heapq import heappop, heappush

Vertex = namedtuple('Vertex', 'frm, to')

def load_dependencies():
    result = []

    got = input()
    while got.lower() != 'end':
        parts = got.split()
        result.append([parts[1], parts[7]])

        got = input()

    return result

def create_graph(dependencies):
    vertexes = {}

    for vert_from, vert_to in dependencies:
        if vert_from not in vertexes:
            vertexes[vert_from] = Vertex(set(), set())

        if vert_to not in vertexes:
            vertexes[vert_to] = Vertex(set(), set())

        vertexes[vert_from].to.add(vert_to)
        vertexes[vert_to].frm.add(vert_from)

    return vertexes

def create_heap(graph):
    heap = []

    for name, vert in graph.items():
        heappush(heap, (len(vert.frm), name, vert))

    return heap

def topsort(graph):
    result = ''

    seen = set()
    heap = create_heap(graph)
    while len(heap) > 0:
        i, popped, vert = heappop(heap)
        if popped in seen:
            continue

        result += popped
        seen.add(popped)

        for removed in vert.to:
            updated = graph[removed]
            updated.frm.remove(popped)
            heappush(heap, (len(updated.frm), removed, updated))

    return result

def solve():
    dependencies = load_dependencies()
    graph = create_graph(dependencies)
    result = topsort(graph)
    print(result)

solve()
