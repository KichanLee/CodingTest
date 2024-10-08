
# num_list = list(range(1, 21))
num_list = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b - a + 1) // 2):
        num_list[b - i], num_list[a + i] = num_list[a + i] , num_list[b - i]

num_list.pop(0)
for x in num_list:
    print(x, end=" ")