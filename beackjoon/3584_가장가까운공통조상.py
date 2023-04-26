import sys
sys.setrecursionlimit(10**5)
T = int(input())
graph = []
first_visited =[]

def dfs(node):
    ## 종료 시점
    if len(graph[node]) == 0:
        return
    
    ## 부모 노드 찾기
    parent = graph[node][0]

    ## 만약 이전에 방문한 적이 있다면 두개 노드가 겹치는 포인트
    if first_visited[parent]:
        print(parent)
        return
    
    ## 겹치지 않는다면 True 해주기
    else:
        first_visited[parent] = True
        dfs(parent)
    

for _ in range(T):
    n = int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a,b = map(int, input().split())
        graph[b].append(a)

    first_visited = [False]*(n+1)

    node1, node2 = map(int, input().split())

    ## 초기 노드 문제
    first_visited[node1] = True
    dfs(node1)

    if first_visited[node2]:
        print(node2)
    else:
        dfs(node2)
    