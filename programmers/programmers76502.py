from collections import deque 
import copy
def solution(s):
    answer = 0
    s = deque(s)
    
    rever = {"(": ")", 
             "[": "]", 
             "{": "}"
            }
    
    ## 후보 s 스택에 넣기
    def breaking(st):
        while st:
            if len(st) == 1:
                return st
                
            elif st[-2] in rever.keys() and st[-1] == rever[st[-2]]:
                st.pop()
                st.pop()
                
            else:
                return st
        return st
            
    
    ## 스택을 채우고
    def check_right(candi):
        nonlocal answer
        repeats = len(candi)
        stacks = []

        while candi:
            stacks.append(candi.popleft())
            stacks = breaking(stacks)
        
        if not stacks:
            answer += 1
            return True
        else:
            return False
    
    
    ## s 회전하기

    for _ in range(len(s)):
        ss = s.popleft()
        s.append(ss)
        candi = copy.deepcopy(s)
        check_right(candi)

    
    return answer
        
        
    
