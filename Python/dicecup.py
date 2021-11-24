inp = input().split()
if  4 <= int(inp[0]) and int(inp[1]) <= 20:
    b = max(int(inp[0]),int(inp[1]))
    k = min(int(inp[0]),int(inp[1]))
    if int(inp[0]) != int(inp[1]):
        
        for i in range(k + 1 , b + 2):
            print(i)


    else:
        print(k+1)
