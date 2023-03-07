

on = dict()

on = {
    "0" : [False]*7,
    "1" : [False]*7,
    "2" : [False]*7,
    "3" : [False]*7,
    "4" :[False]*7,
    "5" :[False]*7,
    "6" :[False]*7,
    "7" :[False]*7,
    "8" :[False]*7,
    "9" : [False]*7,
    " " : [False]*7
 }


for i in range(10):
    a = []
    if i == 1:
        a = [1,2]
    elif i == 2:
        a =[0,1,6,4,3]
    elif i == 3:
        a = [0,1,2,3,6]
    elif i == 4:
        a = [5,6,1,2]
    elif i == 5:
        a = [0,5,6,2,3]
    elif i == 6:
        a = [0,5,4,3,2,6]
    elif i == 7:
        a = [5,0,1,2]
    elif i == 8:
        a = [0,1,2,3,4,5,6]
    elif i == 9:
        a = [0,1,2,5,6,3]
    elif i == 0 :
        a = [0,1,2,3,4,5]
    

    for k in a:
        # print(i,k)
        on[str(i)][k] = True



T = int(input())
test = []

for _ in range(T):
    test.append(list(map(str, input().split())))




def make_long(s):
    return " "*(5-len(s)) + s


for a,b in test:
    cnt = 0
    ## 자리수가 5가 아닌 경우만 다른 조건을 추가해 준다.
    a = make_long(a)
    b = make_long(b)

    for one_num in range(5):
        for line in range(7):
            if on[a[one_num]][line] != on[b[one_num]][line]:
                cnt += 1
    
    print(cnt)