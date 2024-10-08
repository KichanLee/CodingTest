n = int(input())

# gam_list = []

# for _ in range(n):
#     gam_list.append(list(map(int, input().split())))


for i in range(1, n + 1):
    for j in range(i,n + 1):
        if(n % i == 0):
            print('*', end='')
        elif(i % i == 0):
            print('-',end='')

    print()