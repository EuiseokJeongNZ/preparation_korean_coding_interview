from collections import deque

def solution(maps):
    def bfs(s_i, s_j, n, m, visited, maps):
        q = deque([])
        q.append((s_i, s_j))
        visited[s_i][s_j] = True
        
        while q:
            i, j = q.popleft()
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0<=ni<n and 0<=nj<m:
                    if maps[ni][nj] == 1 and not visited[ni][nj]:
                        maps[ni][nj] += maps[i][j]
                        q.append((ni, nj))
                        visited[ni][nj]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*(m+1) for _ in range(n)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    bfs(0, 0, n, m, visited, maps)
    
    if maps[n-1][m-1] == 1:
        return -1

    return maps[n-1][m-1]