import sys
from collections import deque

def dfs(start, graph, visited):
    visited[start] = True
    print(start, end=' ')

    for i in range(1, len(graph[start])):
        if graph[start][i] and visited[i] == False:
            dfs(i, graph, visited)

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')

    while queue:
        curr_point = queue.popleft()
        for i in range(1, len(graph[curr_point])):
            if graph[curr_point][i] and visited[i] == False:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)


input = sys.stdin.readline
if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[False] * (n+1) for _ in range(n+1)]
    visited_dfs = [False] * (n+1)
    visited_bfs = [False] * (n + 1)

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i][j] = True
        graph[j][i] = True

    dfs(v, graph, visited_dfs)
    print()
    bfs(v, graph, visited_bfs)
