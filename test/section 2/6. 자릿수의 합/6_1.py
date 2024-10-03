# 처음 했던 시도

def digit_sum(x):
    
    cnt = 0
    while(x / 10 == 0):
        cnt+=1
    print(cnt)
    max = -1
    for i in range(1, cnt + 1):
        sum += x % 10
    if(sum > max):
        max = sum


a_list = map(int, input().split())


digit_sum(a_list[0])
# 자연수 받고

# 자릿수 갯수 파악하고 자릿수마다 % 10 해서 더해주기

# 제일 큰값 파악하기


# 풀이 보고 풀기 내가 시도해던 방법과 유사

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x //10
    return(sum)

max_val = -1
for x in a:
    total = digit_sum(x)
    if(total > max_val):
        max_val = total
        res = x

print(res)



# 문자열로 쪼개서 풀기

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum