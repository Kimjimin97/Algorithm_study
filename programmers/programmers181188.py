
def solution(targets):
    answer = 0
    targets.sort(key = lambda x : -x[0])
    
    defense = 100000001
    
    for start, end in targets:
        if end <= defense:
            defense = start 
            answer += 1
            
            
    return answer