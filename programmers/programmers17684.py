def solution(msg):
    answer = []
    diction = dict()
    
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
             "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    for a in alpha:
        diction[a] = ord(a) - 64    
    
    idx = 0
    last_num = 26
    search = ""
    
    while idx < len(msg):
        search += msg[idx]
        idx += 1
        if search not in diction.keys():
            last_num += 1
            diction[search] = last_num
            answer.append(diction[search[:-1]])
            search = search[-1]
    
    answer.append(diction[search])            
        
    

    return answer