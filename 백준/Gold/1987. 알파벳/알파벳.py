import sys
from collections import deque

input = sys.stdin.readline

def bfs(s_i, s_j, grid):
    n, m = len(grid), len(grid[0])
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = deque()
    q.append((s_i, s_j, set(grid[s_i][s_j]), 1))  # (i, j, used_letters, length)

    visited = set()
    visited.add((s_i, s_j, tuple(grid[s_i][s_j])))

    max_cnt = 1

    while q:
        i, j, used_letters, length = q.popleft()
        max_cnt = max(max_cnt, length)

        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0<=ni<n and 0<=nj<m:
                ch = grid[ni][nj]
                if not ch in used_letters:
                    new_used_letters = used_letters.copy()
                    new_used_letters.add(ch)
                    state = (ni, nj, tuple(new_used_letters))
                    if not state in visited:
                        visited.add(state)
                        q.append((ni, nj, new_used_letters, length+1))

    return max_cnt


if __name__ == '__main__':
    r, c = map(int, input().split())
    grid = [list(input().strip()) for _ in range(r)]
    print(bfs(0, 0, grid))
