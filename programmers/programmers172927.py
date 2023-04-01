"""

시작시간 06:06
팩토리얼 계산법
1차 풀이 - 06:38 시간 복잡도
2차 풀이 - 07:09 정답

"""
from itertools import permutations

def solution(picks, minerals):
    
    #행은 곡갱이, 열은 광물
    graph = [
        [1,1,1],
        [5,1,1,],
        [25,5,1]
    ]
    
    ## 0 은 다이아몬, 1은 철, 2는 돌
    map_dict = {
        "diamond" : 0,
        "iron" : 1,
        "stone" : 2,
        
    }
    
    items = []

        
    # power += graph[pick][map_dict[minerals[minerals_idx]]]
    min_power = float("INF")
    
    def choose_pick(minerals_idx,power):
        nonlocal min_power
        
        if minerals_idx >= len(minerals) or sum(picks) == 0:
            min_power = min(min_power, power)
            return

        for pick_idx in range(3):
            npower = power
            nminerals_idx = minerals_idx
            
            if picks[pick_idx] != 0:
                picks[pick_idx] -= 1
                
                for i in range(5):
                    if nminerals_idx >= len(minerals):
                        break
                    npower = npower + graph[pick_idx][map_dict[minerals[nminerals_idx]]]
                    nminerals_idx += 1
                
                choose_pick(nminerals_idx, npower)
                picks[pick_idx] += 1
                
    choose_pick(0,0)

    return min_power