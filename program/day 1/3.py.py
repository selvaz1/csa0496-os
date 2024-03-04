input_string = "welcome"
result = ""

for char in input_string:
    if char == 'c':
        continue
    result += char

print(result)
