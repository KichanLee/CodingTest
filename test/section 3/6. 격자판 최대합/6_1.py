n = int(input())

a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))


row_max = 0
col_max = 0
cross_sum = 0
cross_max = 0
# 행렬의 합 최대 구하기
for i in range(n):
    row_sum = 0
    col_sum = 0
    for j in range(n):
        row_sum += a_list[i][j]
        col_sum += a_list[j][i]
        if(i == j):
            cross_sum += a_list[i][j]
    if(row_sum > row_max):
        row_max = row_sum
    if(col_sum > col_max):
        col_max = col_sum
    if(cross_sum > cross_max):
        cross_max = cross_sum
answer_list = [cross_max, row_max, col_max]
print(answer_list)
print(max(answer_list))


# 행의 합 구하기

# 열의 합 최대 구하기

# 대각선 합 최대 구하기