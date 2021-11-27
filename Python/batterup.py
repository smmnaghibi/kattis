n = int(input())
res = 0
count = 0
if 1 <= n <= 100:
    inp = input().split()
    if len(inp) == n:
        for i in inp:
            if 0 <= int(i):
                count += 1
                res += int(i)

print(res/count)
