n = int(input())
num = 2
if 1 <= n <= 15:
    for i in range(n):
        num += 2 ** i
print(num * num)
