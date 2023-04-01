"""
시작시간 - 03:46
1차 제출 - 04:41 [4,5,6,10] - 예상 엣지 케이스 
2차 제출 - 05:30 - 변수 하나를 잘 못 씀


"""
from collections import deque
## 시간을 분으로 만들어주는 함수
def change_min(time_str):
    hour = int(time_str[0:2])
    mint = int(time_str[3:])
    return hour*60 + mint



def solution(plans):
    answer = []
    keep = []
    sort_plans = sorted(plans, key = lambda x : x [1])
    
    for i in range(len(sort_plans)-1):
        now_task, now_start_time, now_take_time = sort_plans[i]
        now_take_time= int(now_take_time)
        
        ## 남은 시간 체크
        remain_time =  change_min(sort_plans[i+1][1]) - change_min(now_start_time) 

        ## 일하고 남은 시간 체크
        remain_time = remain_time - now_take_time
        
        ## 딱 끝냈으면
        if remain_time == 0:
            answer.append(now_task)
        
        ## 시간이 부족하면
        elif remain_time < 0:
            keep.append([now_task, abs(remain_time)])
        
        ## 시간이 남으면
        else:
            answer.append(now_task)
            ## keep에 있는 과목 풀기
            while True:
                if remain_time <= 0 or not keep:
                    break

                keep_task, keep_take_time = keep.pop()
                keep_time = remain_time - keep_take_time

                ## 다 못 끝낸 경우
                if keep_time < 0:
                    keep.append([keep_task, abs(keep_time)])
                    break
                    

                ## 정확하게 끝낸 경우
                elif keep_time == 0:
                    answer.append(keep_task)
                    break

                ## 끝냈는데 시간이 남은 경우
                else:
                    answer.append(keep_task)
                    remain_time = keep_time
    
    ## 마지막 과제는 무조건 추가
    answer.append(sort_plans[-1][0])
    while keep:
        remain_task = keep.pop()
        answer.append(remain_task[0])
    
    return answer