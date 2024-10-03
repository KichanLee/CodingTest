n  = int(input())

score_list = list(map(int, input().split()))

avg = sum(score_list) / n + 0.5

avg = round(avg)
num = 0

min = 2147483649
ans = -1
num = -1
print("avg %d : "%(avg))
for idx, score in enumerate(score_list):
    print("idx : %d score : %d" %(idx, score_list[idx]))
    if(min > abs(avg - score_list[idx])):
        min = abs(avg - score_list[idx])
        num = idx
        ans = score_list[idx]
    elif(min == abs(avg - score_list[idx])):
        if(score_list[idx] > ans):
            ans = score_list[idx]
            num = idx
print(avg, num + 1)