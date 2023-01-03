def solution(s):
    answer = []
    s_list = []
    s = s[2:-2]

    for word_split in s.split("},{"):
        lists = []
        for final_split in word_split.split(","):
            lists.append(int(final_split))
        s_list.append(lists)
    
    s_list.sort(key = lambda x : len(x))
    
    res = []
    
    for ss in s_list:
        for sss in ss:
            if sss not in answer:
                answer.append(sss)

    
    return answer