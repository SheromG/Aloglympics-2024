def stoppedMissiles(n, missiles):

    missiles.sort(key=lambda x: x[1])

    stopped = 0

    lastEndTime =  "00:00:00"

    for missile in missiles:

        startTime, endTime = missile

        if startTime > lastEndTime:

            stopped += 1

            lastEndTime = endTime

    return stopped

for test in range(int(input())):

    n = int(input())

    missiles = [input().split(" - ") for _ in range(n)]

    print(stoppedMissiles(n, missiles))