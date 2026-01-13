import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(s_i, s_j, graph, visited, di, dj):
    visited[s_i][s_j] = 1
    for d in range(4):
        ni = s_i + di[d]
        nj = s_j + dj[d]
        if not (0<=ni<len(graph)) or not(0<=nj<len(graph[0])):
            continue
        if visited[ni][nj] == 0 and graph[ni][nj] == 1:
            dfs(ni, nj, graph, visited, di, dj)

if __name__ == '__main__':
    t = int(input())
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    ans = []

    for _ in range(t):
        m, n, k = map(int, input().split())
        graph = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        cnt = 0

        for _ in range(k):
            j, i = map(int, input().split())
            graph[i][j] = 1

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1 and visited[i][j] == 0:
                    dfs(i, j, graph, visited, di, dj)
                    cnt += 1
        ans.append(cnt)

    for i in range(len(ans)):
        print(ans[i])