from itertools import combinations

MOD = 10 ** 9 + 7

def counter(girders):
    diamonds = 0
    final = []
    
    junctions = []
    for u, v in girders:
        junctions.append((u,v))

    for comb in combinations(junctions, 4):
        numbersDictionary = {}
        
        for tup in comb:
            for num in tup:
                numbersDictionary[num] = numbersDictionary.get(num, 0) + 1
        
            if all(count == 2 for count in numbersDictionary.values()):
                
                if comb[0] not in final:
                    final.append(comb[0])
                    diamonds += 1

    return diamonds

n, m = map(int, input().split())

girder = []
for i in range(m):
    u, v = map(int, input().split())
    girder.append((u,v))

print( counter(girder) % MOD )