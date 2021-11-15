n = int(input())
res = 0

for i in range(n):
    inp = input()
    if 10 <= int(inp) <= 9999:
        mul = (int(inp[:len(inp)-1]) ** int(inp[-1]))
        res += mul
        
print(res)
