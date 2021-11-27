n = int(input())
count = 0
if 1 <= n <= 100:
    inp = input().split()
    if len(inp) == n:
        for i in inp:
            if -1000000 <= int(i) <= 1000000:
                if int(i) < 0:
                    count += 1
print(count)
