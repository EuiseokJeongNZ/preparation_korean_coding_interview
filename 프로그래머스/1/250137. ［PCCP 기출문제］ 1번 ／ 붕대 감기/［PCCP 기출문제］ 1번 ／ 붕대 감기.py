def solution(bandage, health, attacks):
    max_idx = attacks[-1][0]
    
    max_health = health
    curr_attack = 0
    curr_heal = 0
    
    for i in range(1, max_idx+1):
        if i == attacks[curr_attack][0]:
            health -= attacks[curr_attack][1]
            curr_heal = 0
            curr_attack += 1
            if health <=0:
                 return -1
        else:
            health += bandage[1]
            curr_heal += 1
            if curr_heal == bandage[0]:
                health += bandage[2]
                curr_heal = 0
            if health > max_health:
                health = max_health
    
    return health if health>0 else -1