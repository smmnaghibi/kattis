n = int(input())
res = []
if 1 <= n <= 20:

    for i in range(n):

        inp = input()
        lst = inp.split()

        if 1 <= int(lst[0]) <= 10 and len(lst) == int(lst[0]) + 1 :
            res = []
            for i in range(1,len(lst)):

                if 2 <= int(lst[i]) <= 10:

                    res.append(int(lst[i]))
            print(sum(res) - int(lst[0]) + 1)

