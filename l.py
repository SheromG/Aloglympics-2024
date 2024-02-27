import sys
import random

persons = {i: '' for i in range(1, 21)}

potential = []

queryCount = [0]

def query(x, y):
    print(f"QUERY {x} {y}")
    sys.stdout.flush()
    response = input().split()

    if response[0] == "NO":
        del persons[x]

    elif response[0] == "YES" and response[1] == "NO":
        del persons[x]
        del persons[y]

    elif response[0] == "YES" and response[1] == "YES":
        query2(y, x)
    
    queryCount[0] += 1

    return response

def query2(x, y):
    print(f"QUERY {x} {y}")
    sys.stdout.flush()
    response = input().split()
    
    if response[0] == "NO":
        del persons[x]

    elif response[0] == "YES" and response[1] == "NO":
        del persons[x]
        del persons[y]

    elif response[0] == "YES" and response[1] == "YES":
        if x not in potential:
            potential.append(x)
        if y not in potential:
            potential.append(y)

    queryCount[0] += 1

    return response

for index in range(21):
    keys = list(persons.keys())
    key1 = keys[index % len(keys)]
    key2 = keys[(index + 1) % len(keys)]
    
    response = query(key1, key2)

    if len(persons) == 5: 
        print("ANSWER", " ".join(map(str, persons.keys())))
        break

if queryCount[0] > 23:
    randomPerson = random.sample(potential, 5)
    print("ANSWER", " ".join(map(str, randomPerson)))