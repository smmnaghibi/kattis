is_ok = False
x = input().split()
resx = []
resy = []
if 1 <= int(x[0]) <= 1000 and 1 <= int(x[1]) <= 1000:
    resx.append(int(x[0]))
    resy.append(int(x[1]))
    y = input().split()
    if 1 <= int(y[0]) <= 1000 and 1 <= int(y[1]) <= 1000:
        resx.append(int(y[0]))
        resy.append(int(y[1]))
        z = input().split()
        if 1 <= int(z[0]) <= 1000 and 1 <= int(z[1]) <= 1000:
            resx.append(int(z[0]))
            resy.append(int(z[1]))
            is_ok = True
for i in resx:
    if resx.count(i) == 1:
        resxx = i
for j in resy:
    if resy.count(j) == 1:
        resyy = j
if is_ok:
    print(resxx,resyy)
