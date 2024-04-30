import time

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of nodes in the graph
N = len(graph)

def tsp_dfs(graph, start):
    visited = [False] * N
    visited[start] = True

    def dfs(v, count, cost, min_cost):
        if count == N and graph[v][start]:
            return min(min_cost, cost + graph[v][start])
        for i in range(N):
            if not visited[i] and graph[v][i]:
                visited[i] = True
                min_cost = dfs(i, count + 1, cost + graph[v][i], min_cost)
                visited[i] = False
        return min_cost

    min_cost = float('inf')
    min_cost = dfs(start, 1, 0, min_cost)
    return min_cost

# Start node for TSP
start_node = 0

# Measure execution time for DFS
start_time = time.time()
dfs_cost = tsp_dfs(graph, start_node)
dfs_time = time.time() - start_time

print("DFS Cost:", dfs_cost)
print("DFS Execution Time:", dfs_time)
