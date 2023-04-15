def solution(storey):
    answer = 0
    res = storey
    
    i = 1
    
    while res > 0:        
        a = (res%(10**i))//(10**(i-1))
        
        if a < 5:
            answer += a
            res -= a*(10**(i-1))
            
        elif a == 5 :
            i += 1
            b = (res%(10** i))//(10**(i-1))
            i -= 1   
            if b == 5 or b == 9:
                answer += (10 - a)
                res += (10-a)*(10**(i-1))
            else:
                answer += a
                res -= a*(10**(i-1))       
        else:
            answer += (10 - a)
            res += (10-a)*(10**(i-1))
            
        i += 1

    return answer

for g in range(1, 61):
    print(g)