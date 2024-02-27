for test in range(int(input())):
    n = int(input())

    planet_counts = {
            "Mercury": 0,
            "Venus": 0,
            "Earth": 0,
            "Mars": 0,
            "Jupiter": 0,
            "Saturn": 0,
            "Uranus": 0,
            "Neptune": 0,
            "Pluto": 0
        }

    for i in range(n):

        report = input().split()

        for planet in report[2:]:
            if planet in planet_counts:
                planet_counts[planet] += 1

    sortedCounts = sorted(planet_counts.items(), key=lambda x: (-x[1], x[0]))

    for planet, count in sortedCounts:
        print(planet, count)