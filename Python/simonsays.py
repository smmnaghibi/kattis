n = int(input())
if 1 <= n <= 1000:
    for i in range(n):
        inp = input()
        if "Simon says" in inp:
            print(inp[11::])
