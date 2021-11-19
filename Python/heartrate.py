if 1 <= n <= 1000:
    for i in range(n):
        inp = input()
        lst = inp.split()

        if 2 <= int(lst[0]) <= 1000 and 0 < float(lst[1]) < 1000:
            bpm = (60 * int(lst[0])) / float(lst[1])
            abpmm = bpm - 60 / float(lst[1])
            abpmmax = bpm + 60 / float(lst[1])
            print(abpmm,bpm,abpmmax)
