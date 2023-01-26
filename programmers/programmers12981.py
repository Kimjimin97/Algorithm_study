"""

모든 words 탐색
words 를 k로 탐색
만약 k가 n이면
k = 0 사람의 숫자
반복횟수 reapt += 1
"""

def solution(n, words):
    answer = [0,0]
    
    num = 1
    reapt = 1
    
    for i in range(len(words)):
        
        if words[i] in words[:i] or len(words[i]) == 1:
            return [num, reapt]

        
        if words[i][0] != words[i-1][-1] and i != 0:

            return [num, reapt]

        if num == n:
            num = 0
            reapt += 1
            
        num += 1

        
    return answer