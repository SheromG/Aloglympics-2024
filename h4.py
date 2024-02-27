import datetime
from collections import Counter

def calculate(a,b):
    if int(a[:2]) > int(b[:2]):
        return((datetime.datetime.strptime(b, '%H:%M:%S') + datetime.timedelta(hours = 12) - datetime.datetime.strptime(a, '%H:%M:%S')).total_seconds() )
    
    else:
        return((datetime.datetime.strptime(b, '%H:%M:%S') - datetime.datetime.strptime(a, '%H:%M:%S')).total_seconds())

for index in range(int(input())):
    n = int(input())
    a = input().split()[:n]
    b = input().split()[:n]

    print( n - max(Counter([calculate(a[i],b[j]) for i in range(len(a)) for j in range(len(a))]).values()) )