inp = input().split()
if len(inp) == 6:
    if 0 <= int(inp[0]) <= 10 and 0 <= int(inp[1]) <= 10 and 0 <= int(inp[2]) <= 10 and 0 <= int(inp[3]) <= 10 and 0 <= int(inp[4]) <= 10 and 0 <= int(inp[5]) <= 10 :
        print(1 - int(inp[0]),1 - int(inp[1]),2 - int(inp[2]),2 - int(inp[3]),2 - int(inp[4]),8 - int(inp[5]))
