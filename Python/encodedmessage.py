from math import sqrt
n = int(input())
if 0 < n <= 100:
    for i in range(n):
        inp = input()
        if 1 <= len(inp) <= 10000 and inp.isalpha():
#---------------------------------------------------------------------------------
            mat = []
            w = 0
            for i in range(int(sqrt(len(inp)))):
                t = []
                for j in range(int(sqrt(len(inp)))):
                    t.append(inp[w])
                    w+=1
                mat.append(t)
#----------------------------------------------------------------------------------
            res = []
            for i in range(int(sqrt(len(inp)))):
                a = int(sqrt(len(inp)))-1
                tr = []
                for j in range(int(sqrt(len(inp)))):
                    tr.append(mat[a][i])
                    a -= 1
                res.append(tr)
#------------------------------------------------------------------------------------
            resnn = []
            for d in res:
                for dd in d:
                    resnn.append(dd)
            resnn.reverse()
            for d in resnn:
                print(d,end="")
            print()
