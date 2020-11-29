x = int(input())
output = str(x)
while (x != 1):
    if (x % 2):
        x = x * 3 + 1
    else:
        x = int(x / 2)
    output += ' ' + str(x)
print(output.strip())
