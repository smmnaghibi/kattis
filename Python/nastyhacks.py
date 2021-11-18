n = int(input())
lstr = []
if 1 <= n <= 100:
    for i in range(n):
        inp = input()
        lst = inp.split()
        if -(10**6) <= int(lst[0]) <= 10**6 and -(10**6) <= int(lst[1]) <= 10**6 and 0 <= int(lst[2]) <= 10**6:

            if int(lst[1]) - int(lst[2]) > int(lst[0]):
                lstr.append("advertise")
            elif int(lst[1]) - int(lst[2]) == int(lst[0]):
                lstr.append("does not matter")
            elif int(lst[1]) - int(lst[2]) < int(lst[0]):
                lstr.append("do not advertise")

for j in lstr:
    print(j)
