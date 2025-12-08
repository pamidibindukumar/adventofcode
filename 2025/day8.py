from collections import Counter

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n  # how many separate circuits

    def find(self, x):
        # path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # already same circuit, no change
        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def parse_points(filename="ADC2025files/input_day8.txt"):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))
    return points


def squared_distance(a, b):
    return ((a[0] - b[0]) ** 2 +
            (a[1] - b[1]) ** 2 +
            (a[2] - b[2]) ** 2)


def build_sorted_edges(points):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d2 = squared_distance(points[i], points[j])
            edges.append((d2, i, j))
    edges.sort(key=lambda x: x[0])
    return edges


def part1(points, edges, K=1000):
    """Return product of sizes of 3 largest circuits after K closest connections."""
    n = len(points)
    dsu = DSU(n)

    # process first K edges (closest first)
    for idx in range(min(K, len(edges))):
        _, a, b = edges[idx]
        dsu.union(a, b)

    # collect component sizes
    comps = Counter()
    for i in range(n):
        root = dsu.find(i)
        comps[root] = dsu.size[root]

    sizes = sorted(comps.values(), reverse=True)
    prod = 1
    for s in sizes[:3]:
        prod *= s
    return prod


def part2(points, edges):
    """
    Continue connecting closest pairs until all junction boxes
    form a single circuit. Return product of X coordinates of
    the last two junction boxes that needed to be connected.
    """
    n = len(points)
    dsu = DSU(n)
    last_pair = None  # indices (i, j) of last successful union

    for _, a, b in edges:
        merged = dsu.union(a, b)
        if not merged:
            continue  # already in same circuit, skip
        # this connection actually merged two circuits
        last_pair = (a, b)
        if dsu.components == 1:
            break

    if last_pair is None:
        raise RuntimeError("All boxes were already connected?")

    i, j = last_pair
    x1 = points[i][0]
    x2 = points[j][0]
    return x1 * x2


def main():
    points = parse_points("ADC2025files/input_day8.txt")
    edges = build_sorted_edges(points)

    # Part 1 (if you still want it)
    ans1 = part1(points, edges, K=1000)
    print("Part 1: product of sizes of three largest circuits =", ans1)

    # Part 2: product of X coords of last needed connection
    ans2 = part2(points, edges)
    print("Part 2: product of X coordinates of last connection =", ans2)


if __name__ == "__main__":
    main()
