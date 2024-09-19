# 2차원 list 생성 접근

a=[10]*3

#print(a)

#  for _ in range 변수 없이 반복분만 도는 경우
a=[[0]*3 for _ in range(3)]
print(a)

a[0][1] =1
a[1][1] = 2
print(a)


for x in a:
    print(x)  

for x in a:
    for y in x:
        print(y, end =' ')
    print() 