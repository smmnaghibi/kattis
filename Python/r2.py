inp = input().split()
if -1000 <= int(inp[0]) <= 1000 and -1000 <= int(inp[1]) <= 1000:
    temp = int(inp[1]) - int(inp[0])
    print(temp + int(inp[1]))
