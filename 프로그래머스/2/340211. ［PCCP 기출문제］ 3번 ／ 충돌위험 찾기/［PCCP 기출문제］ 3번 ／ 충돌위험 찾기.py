from itertools import zip_longest
from collections import Counter

def direction(robot, route, points, dir): # route, points, dir list
    for i in range(1, len(route)): # [4, 2]
        s_p, e_p = route[i-1], route[i]
        
        s_p_i, s_p_j = points[s_p-1]
        e_p_i, e_p_j = points[e_p-1]
        
        if i == 1:
            dir[robot].append((s_p_i, s_p_j))
        
        while s_p_i != e_p_i:
            if s_p_i < e_p_i:
                s_p_i += 1
            elif s_p_i > e_p_i:
                s_p_i -= 1
            dir[robot].append((s_p_i, s_p_j))
        
        while s_p_j != e_p_j:
            if s_p_j < e_p_j:
                s_p_j += 1
            elif s_p_j > e_p_j:
                s_p_j -= 1
            dir[robot].append((s_p_i, s_p_j))
            

def solution(points, routes):
    answer = 0
    dir = {i+1:[] for i in range(len(routes))}
    
    for robot_num in range(len(routes)):
        direction(robot_num+1, routes[robot_num], points, dir)
        print(len(dir[robot_num+1]))
    
    for positions in zip_longest(*dir.values()):
        positions = [p for p in positions if p is not None]

        counts = Counter(positions)

        for count in counts.values():
            if count >= 2:
                answer += 1
    
    return answer