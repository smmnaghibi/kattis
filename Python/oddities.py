n = int(input())
if 1 <= n <= 20:
    for i in range(n):
        inp = int(input())
        if -10 <= inp <= 10:
            if inp % 2 == 0:
                print(inp,"is even")
            else:
                print(inp,"is odd")
