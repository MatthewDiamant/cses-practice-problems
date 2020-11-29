test_count = int(input())
tests = [[int(n) for n in input().split(' ')] for _ in range(test_count)]

for test in tests:
    y = test[0]
    x = test[1]

    if (x > y):
        start = ((-(-x // 2) * 2) - 1) ** 2
        if (x % 2):
            print(start - y + 1)
        else:
            print(start + y)
    else:
        start = (y // 2 * 2) ** 2
        if (y % 2):
            print(start + x)
        else:
            print(start - x + 1)

