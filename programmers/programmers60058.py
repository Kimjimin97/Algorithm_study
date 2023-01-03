def solution(p):
    answer = ''
    dicts = dict({"(":")", ")":"("})
    
    def balance(s):
        left = 0
        right = 0
        sss = ""
        
        for ss in range(len(s)):
            if s[ss] == "(":
                left += 1
            else:
                right += 1
                
            if left == right:
                return s[:ss+1],s[ss+1:]
        return
    

    def right(s):
        lists = []
        for ss in s:
            if lists and lists[-1] == "(" and dicts[lists[-1]] == ss:
                lists.pop()
                continue
            else:
                lists.append(ss)
        
        if lists:
            return False
        else:
            return True

        return
    
    
    def dfs(s):
        if s == "":
            return ""
        
        u,v = balance(s)
        
        if right(u):
            return u + dfs(v)
            
        else:
            ss = "(" + dfs(v) + ")"
            u = u[1:-1]
            
            for uu in u:
                ss += dicts[uu]
                
            return ss
        

    answer = dfs(p)
    
    
    return answer