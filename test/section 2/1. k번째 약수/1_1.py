
# import sys
# sys.stdin=open("input.txt", "rt")

# # k = int(input())
n ,k = map(int, input().split())
ls = list()

for i in range(1, n + 1):
    # print(i)
    if(n % i == 0):
        ls.append(i)


if((len(ls)) + 1< k ):
    print(-1, end="")
else:
    print(ls[k - 1], end="")


n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        ++cnt
    if cnt == k:
        print(i)
        break
    print(0)


n, k = map(int, input().split())
ls = []

# 1부터 sqrt(n)까지 약수를 구하고 약수를 쌍으로 추가
for i in range(1, int(math.sqrt(n)) + 1): 
    if n % i == 0:
        ls.append(i)  # i는 약수
        if i != n // i:  # i와 n // i가 같지 않을 때만 추가 (중복 방지)
            ls.append(n // i)

# 약수들을 오름차순으로 정렬
ls.sort()

# k번째 약수가 존재하는지 확인
if len(ls) < k:
    print(0)
else:
    print(ls[k - 1])