x = int(input())
res = x
if 1 <= x <= 100:
    n = int(input())
    if 1 <= n <= 100:
        for i in range(n):
            p = int(input())
            if 0 <= p <= 10000:
                res += x - p

print(res)
