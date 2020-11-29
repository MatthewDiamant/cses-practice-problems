n = int(input())
odd_numbers = [x * 2 + 1 for x in range(int(n / 2))]
even_numbers = [x * 2 + 2 for x in range(int(n / 2))]
if (n == 1):
    print("1")
if (n <= 3):
    print("NO SOLUTION")
elif (n % 2):
    print(' '.join([str(n) for n in even_numbers + odd_numbers + [n]]))
else:
    print(' '.join([str(n) for n in even_numbers + odd_numbers]))
