"""
1) 카드 k개 뽑기
2) 중복 확인
"""


n = int(input())

k = int(input())

card = []

for _ in range(n):
    card.append(int(input()))

visited = [False]*n

pick_card = []
res_card =[]
answer = 0

def dfs(cnt):
    global answer
    if cnt == k:
        if ''.join(pick_card) in res_card:
            return
        
        res_card.append(''.join(pick_card))
        answer += 1
        return
    
    for i in range(len(card)):
        if not visited[i]:
            visited[i] = True
            pick_card.append(str(card[i]))
            dfs(cnt + 1)
            pick_card.pop()
            visited[i] = False


dfs(0)
print(answer)


