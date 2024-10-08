# l_size = int(input())

# f_list = []

# map = (int, input().split())

# f_list.append(map)


# t_list = []

# map = (int, input().split())

# t_list.append(map)

# # print(f_list)
# # print(t_list)
# # # tmp_list = f_list + t_list 

# tmp_list.sort()
 

n = int(input())

a_list = list(map(int, input().split()))

m = int(input())

b_list = list(map(int, input().split()))

p1= p2 = 0

c =[]

while p1 < n and p2 < m:
    if(a_list[p1] <= b_list[p2]):
        c.append(a_list[p1])
        p1+=1
    else:
        c.append(b_list[p2])
        p2+=1

if p1<n:
    c = c + a_list[p1:]
if p2<m:
    c = c + b_list[p2:]

print(c)
