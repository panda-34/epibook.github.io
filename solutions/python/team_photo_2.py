# Team_photo_2.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# @include
class GraphVertex:
    def __init__(self):
        self.edges = []
        self.max_distance = 1
        self.visited = False
# @exclude

    def __repr__(self):
        return ('*' if self.visited else '') + '(%d)%d(%s)' % (
            self.max_distance, id(self), ','.join(
                str(id(x)) for x in self.edges))


# @include


def find_largest_number_teams(G):
    return find_longest_path(build_topological_ordering(G))


def build_topological_ordering(G):
    vertex_order = []
    for g in G:
        if not g.visited:
            DFS(g, vertex_order)
    return vertex_order


def find_longest_path(vertex_order):
    max_distance = 0
    while vertex_order:
        u = vertex_order.pop()
        max_distance = max(max_distance, u.max_distance)
        for v in u.edges:
            v.max_distance = max(v.max_distance, u.max_distance + 1)
    return max_distance


def DFS(cur, vertex_order):
    cur.visited = True
    for next in cur.edges:
        if not next.visited:
            DFS(next, vertex_order)
    vertex_order.append(cur)


# @exclude


def main():
    G = [GraphVertex() for i in range(3)]
    G[0].edges.append(G[2])
    G[1].edges.append(G[2])
    assert 2 == find_largest_number_teams(G)


if __name__ == '__main__':
    main()
