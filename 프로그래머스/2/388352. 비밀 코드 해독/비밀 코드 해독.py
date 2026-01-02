from itertools import combinations

def solution(n, q, ans):
    cnt = 0
    m = len(q)
    
    # try every possible secret code candidate (5 numbers from 1 to n)
    for arr in combinations(range(1, n+1), 5):
        check = True # assume this candidate is valid
        for i in range(m):
            temp_cnt = 0 # count matching numbers
            
            # count intersection size between arr and q[i]
            for item in q[i]:
                if item in arr:
                    temp_cnt += 1
            
            # reject candidate if match count differs
            if temp_cnt != ans[i]:
                check = False
                break
        if check:
            cnt += 1
    
    return cnt