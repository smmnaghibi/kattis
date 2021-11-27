n = int(input())
lst = []
if 1 <= n <= 100000:
    inp = input().split()
    for i in inp:
        if len(inp) == n and 0 <= int(i) <= 1000000000:
            lst.append(int(i))
print(inp.index(str(min(lst))))
