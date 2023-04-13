"""
시작시간 - 10:19
종료시간 - 12:01
"""

"""
처음에는 3*3의 빈칸으로 이루어진 게임판에 
선공, 후공이

3개가 같은 표시가 만들어지면 같은 표시를 만든 사람이 승리하고 게임이 종료
9칸이 모두 차서 더 이상 표시할 수 없는 경우에는 무승부로 게임 종료

혼자서
게임이 시작한 후 오와 엑스를 혼자서 번갈아 가면서 표시

그렇게 딕택토 수십 판을 했더니 머쓱이는 게임 도중에 다음과 같은 규칙 실수
1) O를 표시할 차례인데 X를 표시, 반대로 X를 표시할 차례인데 O를 표시
2) 선공이나 후공이 승리해서 게임이 종료 되었음에도 그 게임을 진행

게임판이 규칙을 지켜서 딕택토를 진행했을 때 나올 수 있는 게임 상황이면 1, 아니라면 0을 return
"""
from itertools import permutations
def solution(board):
    answer = -1
    
    boards = [
        list(map(str, b))
        for b in board
    ]
    
    first_pos = []
    after_pos = []
    n = len(boards)
    
    for i in range(len(boards)):
        for j in range(len(boards[0])):
            if boards[i][j] == "O":
                first_pos.append([i,j])
            elif boards[i][j] == "X":
                after_pos.append([i,j])

    first_items = list(permutations(first_pos))
    after_items = list(permutations(after_pos))
    
    
    check_graph = [
        ["." for _ in range(n)]
        for _ in range(n)
    ]
    
    
    
    if len(first_pos) - len(after_pos) < 0:
        return 0
    
    # print(len(first_pos) - len(after_pos))
    elif len(first_pos) - len(after_pos) > 1:
        return 0
        
        
    def inital_graph():
        for i in range(n):
            for j in range(n):
                check_graph[i][j] = "."
                
    
    def check_win():
        ## 가로 
        for i in range(n):
            all_same = True
            start = check_graph[i][0]
            if start == ".":
               
                continue
            for j in range(1,n):
                if check_graph[i][j] != start:
                    all_same = False

            if all_same:
                return True
                
                
        
        ## 세로
        for j in range(n):
            all_same = True
            start = check_graph[0][j]
            if start == ".":
                continue
                
            for i in range(1,n):
                if check_graph[i][j] != start:
                    all_same = False

            if all_same:
                return True
        
        ## 대각선
        start = check_graph[0][0]
        all_same = True
        if start == ".":
            all_same = False
            
        else:
            for i in range(1,n):
                if check_graph[i][i] != start:
                    all_same = False

        if all_same:
            return True
        
        
        start = check_graph[0][n-1]
        all_same = True
        
        if start == ".":
            all_same = False
            
        else:
            for i in range(1,n):
                if check_graph[i][n-i-1] != start:
                    all_same = False
        
        if all_same:
            return True
        
        
        return False
    
    
    total_answer = False
    
    
    for first_item in first_items:
        
        for after_item in after_items:
            
            inital_graph()
            flag = False
            answer_flag = True
            for i in range(len(first_item)):
                
                
                fx, fy = first_item[i]
                check_graph[fx][fy] = "O"
                flag = check_win()
                
                
                if flag:
                    if i < len(first_item) - 1 or i <= len(after_item) - 1:
                        answer_flag= False
                        break
                    

                
                ## 선공이 끝났지만, 후공이 끝나지 않은 경우
                if len(after_item)  < i+1:
                    break
                    
                ax, ay = after_item[i]
                check_graph[ax][ay] = "X"
                flag = check_win()
                
                if flag:

                    if i < len(first_item) - 1 or i < len(after_item) - 1 :
                        answer_flag= False
                        break
                        
            if answer_flag:
                return 1
                    
                    
    
    return 0