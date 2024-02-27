json = {}

for _ in range(int(input())):
    fieldsDictionary = {}
    userType = input().split()

    while True:
        fields = input()

        if fields == '};':
            break
        fieldName, fieldType = fields.split(': ')
        fieldsDictionary[fieldName] = fieldType[:-1]

    json[userType[1]] = fieldsDictionary.copy()

def transform(value, json):
    if value == 'string': return "'string'"
    elif value == 'number': return "0"
    elif value == 'boolean': return "true"
    elif value in json:
        transformed = '{'
        last = len(json[value].items())
        for idx, (key, val) in enumerate(json[value].items()):
            transformed += f"{key}:{transform(val, json)}"
            if idx < last - 1:  
                transformed += ';' 
        transformed += '}'
        return transformed
    else:
        return value

last = json[next(reversed(json))]

print("{", end="")

for key, value in last.items():
    if key != list(last.keys())[-1] : 
        print(f"{key}:{transform(value, json)}" + ";", end="")
    else:
        print(f"{key}:{transform(value, json)}", end="")

print("}", end="")