from collections import defaultdict
from itertools import combinations

def solution(info, query):
    
    def bisect(f_score, f_info):
        
        left, right = 0, len(f_info)-1
        
        while left <= right:
            mid = (left+right) // 2

            if f_info[mid]  >= f_score:
                right = mid - 1
                
            else:
                left = mid + 1
        
        return left
    
    answer = []
    
    score_dict = defaultdict(list)

    for inf in info:
        lan, bf, js, cp, score = inf.split(" ")
        candi = []
        for i in range(5):
            for tuple_candi in  list(combinations([lan, bf, js, cp], i)):
                str_candi = ""
                for one in tuple_candi:
                    str_candi += str(one)
                score_dict[str_candi].append(int(score))
    
    for score in score_dict.keys():
        score_dict[score].sort()
  
    for qu in query:
        str_query = ""
        find_score = int(qu.split(" ")[-1])
        for q in qu.split(" ")[:-1]:
            if q == "-" or q == "and":
                continue
            else:
                str_query += q
        
        find_person_count = len(score_dict[str_query]) - bisect(find_score, score_dict[str_query])
        answer.append(find_person_count)
    
#         for find_score in score_list[find_index:]:
#             for one_person in score_dict[find_score]:
#                 if one_person == str_query:
#                     find_person_count += 1
        
#         answer.append(find_person_count)
    
    
    return answer