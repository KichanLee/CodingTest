n, m = map(int, input().split())
# 4, 6, 8, 12, 20

# 확률이 높은 숫자 출력

answer = list()

for i in range(1, n +1):
    for j in range(1, m + 1):
        answer.append(i + j)

answer.sort(reverse=True)

print(answer)


ans_arr = [0] * (n + m + 3)

for k in answer:
    ans_arr[k] += 1


max_list = []

for i in range(len(ans_arr)):
    if ans_arr[i] == max(ans_arr):
        max_list.append(i)
print(max_list)