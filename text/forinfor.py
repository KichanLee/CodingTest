# for i in range(5):
#     for j in range(5):
#         if(j <= i):
#             print('*', end=' ')
#     print()
for i in range(5):
    for j in range(5, i, -1):
            print('*', end=' ')
    print()
for i in range(5):
    for j in range(5 - i):
            print('*', end=' ')
    print()