# lambda function

#  익명 함수

# def plus_one(x):
#     return (x + 1)

# print(plus_one(1))

# plus_two=lambda x: x+ 2

# print(plus_two(1))


# a= [1, 2, 3]
# print(list(map(plus_one, a)))

def plus_one(x):
    return x + 1

a=[1, 2, 3]
print(list(map(plus_one, a )))

print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))

# sort 해줄때 어떤 기준으로 정렬해주는지에 따라 많이 사용