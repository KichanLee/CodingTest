msg="It is show time"
print(msg.lower())
print(msg.upper())

tmp = msg.upper();
print(tmp)
print(tmp.find('T'))

print(msg);

print(msg[:4])
print(msg[3:5])

print(len(msg))

for i in range(len(msg)):
    print(msg[i])
for x in msg:
    print(x, end='')
print()

for x  in msg:
    if x.isupper():
        print(x, end='')

for x in msg:
    if(x.isalpha()):
        print(x, end='')
print()

# org는 ascii넘버를 출력함
tmp ='AZ'
for x in tmp:
    print(ord(x)) 

tmp = 65
# print(char(tmp))
#  char 이 아니라 chr()

tmp = 65
print(chr(tmp))