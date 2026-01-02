def solution(schedules, timelogs, startday):
    # schedules: desired start time for each employee
    # timelogs: actual arrival times for each employee over the week
    # startday: day of the week when the event starts (1~7)
    # saturday and sunday are excluded from evaluation

    
    def to_min(t): # helper method: convert HHMM to minutes
        return (t // 100) * 60 + (t % 100)
    
    cnt = 0
    n = len(schedules)
    m = len(timelogs[0])
    gift = [0]*n
    
    for i in range(n):
        due_time = to_min(schedules[i]) + 10
        curr_day = startday
        for j in range(m):
            arrival_time = to_min(timelogs[i][j]) 
            
            if curr_day != 6 and curr_day != 7: # skip weekends
                if arrival_time <= due_time:
                    gift[i] = 1
                else:
                    gift[i] = 0
                    break
            curr_day += 1
            if curr_day > 7:
                curr_day %= 7
                
        if gift[i] == 1:
            cnt += 1
            
    return cnt