from collections import deque

empty = '0'

def crane(grid, target):
    removed = 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == target:
                grid[i][j] = empty
                removed += 1
    return removed

def bfs(grid, si, sj):
    n, m = len(grid), len(grid[0])
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    q = deque()
    visited = [[False] * m for _ in range(n)]

    for di, dj in dirs:
        ni, nj = si + di, sj + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
            return True
        if grid[ni][nj] == empty:
            q.append((ni, nj))

    while q:
        r, c = q.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True

        for di, dj in dirs:
            nr, nc = r + di, c + dj
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                return True
            if not visited[nr][nc] and grid[nr][nc] == empty:
                q.append((nr, nc))

    return False

def forklift(grid, target):
    r, c = len(grid), len(grid[0])
    to_remove = []

    for i in range(r):
        for j in range(c):
            if grid[i][j] != target:
                continue
            if bfs(grid, i, j):
                to_remove.append((i, j))

    for i, j in to_remove:
        grid[i][j] = empty

    return len(to_remove)

def solution(storage, requests):
    r, c = len(storage), len(storage[0])
    grid = [list(row) for row in storage]
    remaining = r * c

    for request in requests:
        if len(request) == 2:
            remaining -= crane(grid, request[0])
        else:
            remaining -= forklift(grid, request[0])

    return remaining
