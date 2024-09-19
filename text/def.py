'''
function making
'''

# def add(a, b):
#     c= a + b
#     print(c)

# add(3, 2)
# add(5, 7)


def add(a, b):
    c = a + b
    d = a - b
    return c, d

print(add(10, 1 ))

a =[12, 13, 7, 9, 19]

def isPrime(x):
    for i in range(2, x):
        if(x % i == 0):
            return False
        return True
    
a = [12, 14, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end =' ')