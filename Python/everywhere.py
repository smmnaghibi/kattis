t = int(input())
lst = []
res = []
if t <= 50:
    for i in range(t):

        size = int(input())
        if size <= 100:
            for i in range(size):
                inp = input()
                if 1 <= len(inp) <= 20 and inp.islower() and not inp.isspace():
                    lst.append(inp)
                lstr = []
                for i in lst:
                    if i not in lstr:
                        lstr.append(i)
            res.append(len(lstr))
            lstr.clear()
            lst.clear()

for i in res:
    print(i)
