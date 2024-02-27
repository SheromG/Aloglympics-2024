answer = {}

for index in range(int(input())):

    n = int(input())
    s = list(map(int, input().split()))

    answer = {i + 1: s[i] for i in range(n)}

    output = ""

    for i in range(1, n + 1):
        nextIndex = None
        nextSkill = float('inf')

        for j in range(i + 1, n + 1):

            if answer[j] > answer[i] and answer[j] < nextSkill:
                nextSkill = answer[j]
                nextIndex = j

        if nextIndex: output += str(nextIndex) + " "

        else: output += str(i) + " " 

    print(output)