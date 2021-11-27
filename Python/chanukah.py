n = int(input())

if 1 <= n <= 10000:
    for i in range(1,n+1):
        inp = input().split()
        if int(inp[0]) == i and 1 <= int(inp[1]) <= 10000:
            jam = 0
            for j in range(1,int(inp[1])+1):
                jam += j

        print(i,jam+int(inp[1]))
