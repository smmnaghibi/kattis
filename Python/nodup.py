inp = input()
lst = inp.split()
ist = True
if len(inp) <= 80:
    for i in lst:
        if 1 < lst.count(i):
            ist = False
if ist:
    print("yes")
else:
    print("no")
