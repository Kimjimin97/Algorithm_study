"""
투포인터
"""
from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while answer < 2*(len(queue1) + len(queue2))-1:

        if sum1 == sum2:
            break
            
        answer += 1

        if sum1 > sum2:
            data = q1.popleft()
            q2.append(data)
            sum1 -= data
            sum2 += data
        else:
            data = q2.popleft()
            q1.append(data)
            sum1 += data
            sum2 -= data

    
    if sum1 != sum2 or (q1 == queue2 and q2 == queue1):
        answer =-1
        
    return answer