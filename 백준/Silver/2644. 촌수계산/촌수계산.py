import sys
from collections import defaultdict

input = sys.stdin.readline

def dfs(start, target, cnt, graph, visited):
    if start == target:
        return cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            res = dfs(i, target, cnt + 1, graph, visited)
            if res != -1:
                return res
    return -1

if __name__ == '__main__':
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    graph = defaultdict(list)
    visited = [False]*(n+1)

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    print(dfs(a, b,0, graph, visited))