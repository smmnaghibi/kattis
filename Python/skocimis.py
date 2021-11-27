inp = input().split()
if 0 < int(inp[0]) < int(inp[1]) < int(inp[2]) < 100 and len(inp) == 3:
    x = int(inp[1]) - int(inp[0]) - 1
    y = int(inp[2]) - int(inp[1]) - 1
    if x > y and 0 < x :
        print(x)
    else:
        print(y)
