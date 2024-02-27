for test in range(int(input())):

    dictionary = {}

    alphabet = input().split()

    designated = map(int, input().split())

    for letter, designation in zip(alphabet, designated):
        dictionary[letter[0]] = designation

    for index in range(int(input())):
        word = input()

        total = 0

        for letter in word:
            if letter in dictionary:
                total += dictionary[letter]

        if total > 0:
            print("POSITIVE")
        elif total < 0:
            print("NEGATIVE")
        elif total == 0:
            print("NEUTRAL")