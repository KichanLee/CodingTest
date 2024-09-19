'''
반복문 for, while
'''

# a = range(10)

# # 1, 10까지 순차적으로 만들어주는 함수

# print(list(a)) 

# for i in range(1, 11):
#     print(i)
    # 1부터 10까지 만들어주는 함수
# for i in range(10):
#     print(i)
#     # 0부터 9까지 만들어주는 함수

# for i in range(10, 0, -1):
#     print(i)
# 2씩 작아지는 부분



# i = 1
# while (i <= 10):
#     print(i)
#     i += 1
i = 1
# while True:
#     print(i)
#     if i == 4:
#         break
#     i+=1


for i in range(1, 5):
    if(i % 2 == 0):
        continue;
    else:
        print(i ,',' '홀수')
