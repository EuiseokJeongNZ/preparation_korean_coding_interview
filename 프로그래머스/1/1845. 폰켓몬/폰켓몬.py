def solution(nums):
    dic = {}
    max_len = 0
    
    for n in nums:
        if n not in dic:
            dic[n] = 1
    
    max_len = len(dic)
    
    if max_len > len(nums) // 2:
        return len(nums) // 2
    
    return max_len