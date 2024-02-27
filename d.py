for test in range(int(input())):
    s,n = map(int, input().split())

    order = input().split()

    order = list(map(int, order[:n]))

    rotations = [order[i:] + order[:i] for i in range(len(order))]

    checker = []

    for i in range(s):
        serve = input().split()

        serveIntegers = list(map(int, serve[:n]))
        checker.append(serveIntegers)

    for i, sublist in enumerate(checker):
        if sublist in rotations:
            index = i + 1
            break

    print(index)