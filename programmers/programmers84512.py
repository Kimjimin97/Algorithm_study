from collections import deque

def solution(n, k):
    
    def isSo(check_num):
        if int(check_num) == 1 or int(check_num) == 0:
            return False
        
        for i in range(2, sqrt(int(check_num))):
            if int(check_num) % i == 0:
                return False
        return True

    
    
    change = ''
    cnt = 0
    while n >= 1:
        change = str(n % k) + change
        if n % k == 0:
            if isSo(change):
                cnt += 1
            change = ""
        n = n // k
    
    if isSo(change):
        cnt += 1
   
    return cnt