a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:5])

for i in range(len(a)):
    print(a[i], end ='  ')

print()

for x  in a :
    print(x, end=' ')

#  튜플
for x in enumerate(a):
    print(x)
b = (1, 2, 3, 4, 5) 
# b[0]= 7
#  튜플은 값 변경이 불가능함

for x in enumerate(a):
    print(x[0], x[1])
for index, value in enumerate(a):
    print(index, value)

# 모두가 참일때만 참임
if all(60 < x for x in a):
    print("yes")
else:
    print("no")
# 한가지라도 참이면 참
if any(60 < x for x in a):
    print("yes")
else:
    print("no")