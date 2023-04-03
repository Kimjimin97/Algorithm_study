"""
시작시간 - 11:00
종료시간 - 14:18
반올림 round(12.4,2)
sqrt 왜 반올림 해주는가?
문제의 조건식 같은 행 혹은 열에 있는 경우 고려해주김
"""
from math import sqrt

def solution(m, n, startX, startY, balls):
    
    def rotate(x1,y1,x2,y2,k):
        if k == 0:
            return [x1,y1,x2,y2]
        
        if k == 1: 
            return [y1,x1,y2,x2]
        
        if k == 2:
            return [n-x1, y1, n-x2, y2]
        
        if k == 3:
            return [m-y1,x1,m-y2,x2]
    
        return
    
    def calculate(x1,y1,x2,y2):
        
        
        row = abs(y2-y1)
        a = row*x1 / (x2 + x1)
        
        if x1 < x2 and y1== y2:
            return (2*n+2*m)**2
        

        return round((sqrt(a**2+(x1)**2) + sqrt((row-a)**2+x2**2))**2,0)
    
    
    answer = []
    for x1,y1 in balls:
        min_length = float("INF")
        x2 = startX 
        y2 = startY
        for k in range(4):
            x1,y1, x2, y2 = rotate(x1, y1,x2,y2,k)
            min_length = min(min_length, calculate(x1,y1, x2, y2))
        
            
        answer.append(min_length)
        
        
    
    
    return answer