# 점수의 평균을 구하고, 평균에 가장 가까운 학생은 몇번째인지 출력
# 가까운점수가 여러개인 경우, 점수 > 학생번호 순

n = int(input())
score_list = list(input().split())

sum = 0
for index, value in enumerate(score_list):
    sum += value
    print(index, value)
avg = sum / index


print('sum : %d'  %(sum))
# print('idx : %d'  %(index)) 
# print('Avg : %d'  %(avg))

# 평균과 가까운 점수 찾

for index, value in enumerate(score_list):
    min = score_list[0]
    if(min - avg == 0):
        print()
    if(min < abs(avg - score_list[0])):
        min = score_list[index]
    



    
