import sys
sys.setrecursionlimit(10**6)


def dfs(i, j, cnt, visited, land, di, dj, columns):
    visited[i][j] = True
    columns.add(j)
    
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < len(land) and 0 <= nj < len(land[0]):
            if not visited[ni][nj] and land[ni][nj] == 1:
                cnt = dfs(
                    ni, nj,
                    cnt + 1,
                    visited, land,
                    di, dj,
                    columns
                )

    return cnt


def solution(land):
    n = len(land)
    m = len(land[0])

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    visited = [[False] * m for _ in range(n)]
    cnt = [0] * m
    
    for j in range(m):
        for i in range(n):

            if land[i][j] == 1 and not visited[i][j]:
                columns = set()

                temp = dfs(
                    i, j, 1,
                    visited, land,
                    di, dj,
                    columns
                )
                
                for column in columns:
                    cnt[column] += temp

    return max(cnt)