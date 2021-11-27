inp = input()
lst = inp.split()
res = []
for i in lst:
    for j in i:
        if j.isupper():
            res.append(j)

for k in res:
    print(k,end="")
