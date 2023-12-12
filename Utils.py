import heapq
from collections import deque


def dfs(adj, v, parent, order):
    if not parent:
        parent[v] = None
    # checking neighbours of v
    for n in adj[v]:
        if n not in parent:
            parent[n] = v
            dfs(adj, n, parent, order)

    # we're done visiting a node only when we're done visiting
    # all of its descendants first
    order.append(v)


def topological_sort(adj):
    parent = {}
    order = []
    for v in adj.keys():
        if v not in parent:
            parent[v] = None
            dfs(adj, v, parent, order)

    return list(reversed(order))


def dag_shortest_path(adj, source, dest):
    order = topological_sort(adj)
    parent = {source: None}
    d = {source: 0}

    for u in order:
        if u not in d:
            continue  # get to the source node
        if u == dest:
            break
        for v, weight in adj[u]:
            if v not in d or d[v] > d[u] + weight:
                d[v] = d[u] + weight
                parent[v] = u

    return parent, d


def dijkstra(adj, start, target):
    d = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    visited = set()
    while pq:
        du, u = heapq.heappop(pq)
        if u in visited:
            continue
        if u == target:
            break
        visited.add(u)
        for v, weight in adj[u]:
            if v not in d or d[v] > du + weight:
                d[v] = du + weight
                parent[v] = u
                heapq.heappush(pq, (d[v], v))

    return parent, d


def bfs(adj, s):
    parent = {s: None}
    d = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        for n in adj[u]:
            if n not in d:
                parent[n] = u
                d[n] = d[u] + 1
                queue.append(n)
        return parent, d


def bellman_ford(adj, s):
    parent = {s: None}
    d = {s: 0}
    queue = deque()
    queue.append(s)
    in_queue = {s}

    counter = {}

    while queue:
        u = queue.popleft()
        in_queue.remove(u)

        for n, weight in adj[u]:
            # have to relax the edge first, whether or not the node was in the queue
            if n not in d or d[n] > d[u] + weight:
                d[n] = d[u] + weight
                parent[n] = u

                if n not in in_queue:
                    queue.append(n)
                    in_queue.add(n)
                    counter[n] = counter.get(n, 0) + 1

                    if counter[n] >= len(adj):
                        print("Negative Cycle detected")
                        return

        return parent, d
