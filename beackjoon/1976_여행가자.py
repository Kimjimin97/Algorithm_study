"""
동혁이는 친구들과 함께 여행을 간다.
n의 도시
중간에 다른 도시를 경유해 여행을 할 수도 있다.

여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능하지
여부를 판별하는 프로그램을 작성하세요

"""


n = int(input())
m = int(input())


graph = [
    list(map(int, input().split()))
    for _ in range(n)
]


path = list(map(int, input().split()))


parent = [i for i in range(n)]




## union
def union(a,b):
    a = find(a)
    b = find(b)
    # print("a",a,"b",b,"parent_A",parent_a,"parent_b",parent_b)
    if a < b:
        parent[a] = b
    
    else:
        parent[b] = a

## find
def find(node):
    if parent[node] != node:
        return find(parent[node])
    return node

def solution(node):
    ## 연결된 노드를 확인한다.
    for i in range(n):
        ## 연결된 노드가 최상단 부모 노드라면, 개신해준다.
        if graph[node][i] == 1:
            union(node, i)
    return 


for i in range(n):
    solution(i)


flag= True
for i in path:
    if find(parent[i-1]) != find(parent[path[0]-1]):
        flag = False
        print("NO")
        break



# print(parent)

if flag:
    print("YES")