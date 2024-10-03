# n개의 숫자로 이루어진 숫자열


# 첫번째 줄은 s, e, k 가 차례로 주어진다.

# s 번째 부터 e 번째까지의 수를 오름차순 정렬시
# k번째로 나타나는 숫자

t = int(input())

for _ in range(t):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    tmp_list = a[s-1:e]
    tmp_list.sort()
    print("#%d %d" %(t -1 , tmp_list[k-1]))
