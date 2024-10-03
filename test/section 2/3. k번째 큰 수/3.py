
n, ks = map(int, input().split())

ls = list(map(int, input().split()))
sum = 0
sum_set = set()
# set 자료구조는 중복을 허용하지 않음
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum_set.add(ls[i] + ls[j] + ls[k])

sum_ls = list(sum_set)
sum_ls.sort(reverse=True)
print(sum_ls[ks-1])

