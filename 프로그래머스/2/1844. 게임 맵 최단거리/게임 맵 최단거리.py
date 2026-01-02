from collections import deque

def solution(maps):
    def bfs(i, j):
        q = deque([(i, j)])
        visited[i][j] = True
        
        while q:
            i, j = q.popleft()
            
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0<=ni<len(maps) and 0<=nj<len(maps[0]):
                    if maps[ni][nj] == 1 and not visited[ni][nj]:
                        maps[ni][nj] += maps[i][j]
                        q.append((ni, nj))
                        visited[ni][nj] = True
        return
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visited = [[False]*(len(maps[0])) for _ in range(len(maps))]
        
    bfs(0, 0)
    
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        return -1
    
    return maps[len(maps)-1][len(maps[0])-1]