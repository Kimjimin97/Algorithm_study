def solution(numbers, target):
    answer=0
    cnt=0
    num = len(numbers)
    list1=[]
    def dfs(cnt,result):
        if len(list1)==num:
            if result == target:
                anwer+=1

        dfs(cnt+1,result+numbers[num])
        dfs(cnt+1,result-numbers[num])

    dfs(0,0)
    return answer