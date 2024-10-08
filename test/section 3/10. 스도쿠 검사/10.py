n = int(input())
mt = []

for i in range(n + 2):
    mt.append([0] * (n + 2))

ans = []
i = 0
for i in range(n):
    ans.append(list(map(int, input().split())))


print(ans)
print(mt)

i = 0
j = 0
for i in range(n):
    for j in range(n):
        mt[i + 1][j + 1] = ans[i][j]

i = 0
j = 0

def check_top(i, j):
    if(mt[i][j] > mt [i][j - 1] and mt[i][j] > mt[i - 1][j] and mt[i + 1][j] < mt[i][j] and mt[i][j + 1] < mt[i][j]):
        return True
    return False

sum = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if(check_top(i, j)):
            sum +=1

print(sum)
