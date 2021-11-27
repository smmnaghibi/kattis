inp = input().split()
if 0 <= int(inp[0]) <= 23 and 0 <= int(inp[1]) <= 59:
    if int(inp[1]) - 45 < 0 and 0 <= int(inp[0]) - 1 :
        print(int(inp[0])-1,60-45+int(inp[1]))
    elif int(inp[0]) - 1 == -1:
        print(23,60-45+int(inp[1]))
    else:
        print(int(inp[0]),int(inp[1])-45)
