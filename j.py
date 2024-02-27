def hv(operation, a, b):
    if operation[0] == 'H'and operation[1] == 'A':
        index1 = int(operation[2]) - 1
        index2 = int(operation[3]) - 1
        a[index1], a[index2] = a[index2], a[index1]
    elif operation[0] == 'H'and operation[1] == 'B':
            index1 = int(operation[2]) - 1
            index2 = int(operation[3]) - 1
            b[index1], b[index2] = b[index2], b[index1]
    elif operation[0] == 'V':
        index = int(operation[1]) - 1
        a[index], b[index] = b[index], a[index]

def lrc(l, r, c, a, b):
    result = c
    for i in range(r, l-1, -1):
        result = (a[i]*result + b[i]) % 998244353
    return result

n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

q = int(input())

operations = []

for index in range(q):
    operation = input().split()
    
    if operation[0] == '?':
        l, r, c = map(int, operation[1:])
        print(lrc(l - 1, r - 1, c, a, b))
        
    else:
        hv(operation, a, b)