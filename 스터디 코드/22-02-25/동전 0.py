#문제
#https://www.acmicpc.net/problem/11047


#풀이
a, b = map(int,input().split())
li = []
for i in range(a):
    c = int(input())
    li.append(c)
li.sort(reverse=True)
cnt = 0
while True:
    if li[0] > b:
        li.pop(0)
    else:
        if b // li[0] == b / li[0]:
            cnt += b // li[0]
            break
        else:
            cnt += b // li[0]
            b = b % li[0]
            li.pop(0)
print(cnt)