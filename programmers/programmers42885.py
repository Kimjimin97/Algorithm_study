from collections import deque

def solution(people, limit):
    answer = 0
    
    queue = deque()
    people.sort(reverse = True)
    for i in people:
        queue.append(i)

    boat = queue.popleft()
    cnt = 1
    while queue: 
        test = boat + queue[-1]
        if test > limit:
            cnt += 1
            if queue:
                boat = queue.popleft()
        else:
            boat += queue.pop()     
    
    return cnt