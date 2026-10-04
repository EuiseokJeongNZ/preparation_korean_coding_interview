def sec(str):
    mm, ss = str.split(":")
    mm, ss = int(mm), int(ss)
    sec = mm*60 + ss
    return sec

def mm_ss(sec):
    mm = str(sec//60)
    ss = str(sec%60)
    if len(ss)==1:
        ss = '0'+ss
    if len(mm)==1:
        mm = '0'+mm
    return mm+":"+ss

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    sec_video_len = sec(video_len)
    sec_pos = sec(pos)
    sec_op_start = sec(op_start)
    sec_op_end = sec(op_end)
    
    if sec_op_start <= sec_pos <= sec_op_end:
        sec_pos = sec_op_end
    
    for command in commands:
            
        if command == 'next':
            sec_pos += 10
            if sec_pos > sec_video_len:
                sec_pos = sec_video_len
        elif command == 'prev':
            sec_pos -= 10
            if sec_pos < 0:
                sec_pos = 0
        
        if sec_op_start <= sec_pos <= sec_op_end:
            sec_pos = sec_op_end
        
    answer = mm_ss(sec_pos)
    return answer