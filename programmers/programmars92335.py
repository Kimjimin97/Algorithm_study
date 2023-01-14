import math
def solution(n, k):
    answer = 0
    
    def check(k):
        ## 진수 1 처리 해주기
        if k == 1:
            return False 
        for i in range(2, int(math.sqrt(k)) +1):
            if k%i == 0:
                return False
        return True

    change= ""
    def make_jinsu(n,k):
        nonlocal change
        if n < k :
            change += str(n)
            return change
        
        make_jinsu(n//k,k)
        change += str(n%k)
        return change
    
    
    
    make_jinsu(n,k)
    item = change.split("0")
    
  
    
    for it in item:
        # print(it)
        if it and check(int(it)):
            answer += 1

    
    
    return answer