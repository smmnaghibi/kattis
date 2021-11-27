n = int(input())
if 1 <= n <= 1000:
    for i in range(n):
        inp = input()
        if inp == "P=NP":
            print("skipped")
        else:
            x = inp.split("+")
            for j in x:
                if 0 <= int(j) <= 1000:
                    print(int(x[0])+int(x[1]))
                    break
