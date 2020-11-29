n = int(input())
numbers = sorted([int(x) for x in input().split(' ')])
while(len(numbers) and numbers.pop() == n):
    n -= 1
print(n or 1)
