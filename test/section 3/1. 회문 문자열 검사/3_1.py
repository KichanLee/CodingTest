
n = int(input())

def check_word(word):
    i = 0
    reverse_word=""
    for i in range(len(word) -1 , -1, -1):
        reverse_word += str(word[i])
    print("reverse_word : %s" %(reverse_word))
    print("word : %s " %(word))
    if(reverse_word == word):
        return True
    else:
        return False

answer_list = list()

for i in range(n):
    word = input()
    if(check_word(word)):
        answer_list.append("YES")
    else:
        answer_list.append("NO")

print(answer_list)



n = int(input())

for i in range(n):
	s = input()
	s = s.upper()
	size = len(s)
	
	for j in range(size /2 ):
		if s[j] != s[-1-j]:
			print("#%d NO")