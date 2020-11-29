_ = input()
numbers = [int(n) for n in input().split(' ')]
steps = 0
last = 0
for n in numbers:
    if (not (n >= last)):
        steps += last - n
    else:
        last = n
print(steps)
