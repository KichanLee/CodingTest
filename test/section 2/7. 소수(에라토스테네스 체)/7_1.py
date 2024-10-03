
# 소수구하기 
# 소수란? 1과 자기 자신을 제외하고는 약수가 없는 수
# 2, 3, 5, 7, 11, ...

# 2 부터 n 까지 소수의 갯수 구하기
n = int(input())
a_list = list()
# 내가 작성한 
for i in range(2, n + 1):
    if n % i == 0:
        continue;
    a_list.append(i)

print(len(a_list))
