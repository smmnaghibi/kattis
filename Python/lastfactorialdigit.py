t = int(input())
if 1 <= t <= 10:
    for i in range(t):
        inp = int(input())
        res = 1
        if 0 <= inp <= 10:

            for j in range(1,inp+1):
                res *= j
                ress = str(res)
        print(ress[-1])
