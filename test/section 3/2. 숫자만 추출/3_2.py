
word = input()
number_list = ""


for i in range(len(word)):
    if( '0' <= word[i] <='9'):
        number_list += word[i]
# int(number_list)

if(number_list[0] == '0'):
    number_list = number_list[1:]
number_list = int(number_list)
print(number_list)

# 약수의 갯수
cnt =0
for j in range(1, number_list + 1):
    if(number_list % j == 0):
        cnt +=1
print(cnt)        

