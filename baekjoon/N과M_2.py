
N,M = map(int, input().split())

a = []

visited = [False]*(N+1)

def back2(s):
    global a
    if len(a) == M:
        print(*a)
        return
    
    for i in range(s,N+1):
        if not visited[i]:
            visited[i] = True
            a.append(i)
            back2(i+1)
            a.pop()
            visited[i] = False

back2(1)
