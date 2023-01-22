def solution(str1, str2):
    answer = 0
    
    
    def make_dict(stri, num):
        for i in range(len(stri)-1):
            s = stri[i] + stri[i+1]
            
            
            if s.isalpha():
                s = s.lower()
                if s in str_dict.keys():
                    str_dict[s][num] += 1
                else:
                    str_dict[s] = [0,0]
                    str_dict[s][num] += 1
        return 
    
    str_dict = dict()
    make_dict(str1,0)
    make_dict(str2,1)
    
    hap = 0
    geo = 0
    for x in str_dict.keys():
        hap += max(str_dict[x][0], str_dict[x][1])
        
        if str_dict[x][0] >= 1 and str_dict[x][1] >= 1:
            geo += min(str_dict[x][0], str_dict[x][1])
    
    if len(str_dict) == 0:
        return 65536
    else:
        return int(geo/hap * 65536)