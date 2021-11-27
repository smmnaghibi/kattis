res = []
l = input()
if 1 <= int(l) <= 10000:
    d = input()
    if 1 <= int(d) <= 10000 and 1 <= int(l) <= int(d) and 1 <= int(d):
        x = input()
        if 1 <= int(x) <= 36:
            for i in range(int(l),int(d)+1):
                lst = []
                for j in str(i):
                    lst.append(int(j))
                if sum(lst) == int(x):
                    res.append(i)

print(min(res))
print(max(res))
