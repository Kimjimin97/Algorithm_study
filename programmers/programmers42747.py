def solution(citations):
    if sum(citations) == 0:
        cnt = 0
        return cnt
        
    for i in range(len(citations),0,-1): # h편의 논문
        cnt = 0
        for j in citations: # h편 이상 인용
            if j >= i:
                cnt += 1 # h편 이상 인용된 논문의 갯수
        
        if i <= cnt:
            return i