def solution(arr):
    answer = [0,0]
    
    def dfs(N,sx,sy):
        if N ==  1:
            return arr[sx][sy]
            
        a = dfs(N//2, sx, sy)
        b = dfs(N//2, sx, sy+N//2)
        c = dfs(N//2, sx+N//2, sy)
        d = dfs(N//2, sx+N//2, sy+N//2)
        
        ## 같은 경우 -> return a
        if a == b and b == c and c == d and a != -1:
            return a
        
        else:
            if a != -1:
                answer[a] += 1
            if b != -1:
                answer[b] += 1
            if c != -1:
                answer[c] += 1
            if d != -1:
                answer[d] += 1
            ## 다른 경우 경우는 -1을 return    
            return -1
    
    ans = dfs(len(arr),0,0)
    if ans != -1:
        answer[ans] += 1
    
    return answer