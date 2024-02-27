for test in range(int(input())):
    r,c = map(int, input().split())
    grid = [input() for _ in range(r)]

    row = []
    col = []

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'X':
                row.append((i, j))
                col.append((j, i))

    index = set(index[0] for index in row)
    index2 = set(index[0] for index in col)

    count = min(len(index),len(index2))
    print(count)  