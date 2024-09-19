import random as r

a=[]
print(a)
b = list()
print(b)

a = [1,2, 3, 4, 5]

# print(a)
# print(a[0])

# b = list(range(1, 113))

# c = a + b

# print(c)

# a.append(10)

# print(a)

a.insert(3, 7);
print(a)
# 3번 인덱스 지점에 삽입하기

a.pop()
# last delete
print(a)
a.pop(3)
print(a)

a.remove(4)

print(a)

print(a.index(1))  # 5의 인덱스값을 확인하여 출력해준다.

a = list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
# min 은 인자값중 최대값을 출력해준다.

r.shuffle(a)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.clear()
print(a)