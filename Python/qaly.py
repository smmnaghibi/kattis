n = int(input())
ress = 0
if 1 <= n <= 100:
    for i in range(n):
        inp = input()
        inpl = inp.split()

        if 0 < float(inpl[0]) <= 1 and 0 < float(inpl[1]) <= 100:
            mul = float(inpl[0]) * float(inpl[1])
            ress += mul

print(float(ress))
