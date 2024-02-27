answers = []

for _ in range(int(input())):

    n = int(input())
    s = list(map(int, input().split()))

    answers.append((n, s))

for n, s in answers:
    output = ""
    for i in range(1, n + 1):
        nextIndex = None
        nextSkill = float('inf')

        for j in range(i + 1, n + 1):
            if s[j - 1] > s[i - 1] and s[j - 1] < nextSkill:
                nextSkill = s[j - 1]
                nextIndex = j

        if nextIndex:
            output += str(nextIndex) + " "
        else:
            output += str(i) + " " 

    print(output)
