inp = input()
lst = inp.split()

if 2 <= int(lst[0]) <= 10000 and 0 < int(lst[1]) < int(lst[0]) and 0 < int(lst[2]) < int(lst[0]):

    if int(lst[0]) - int(lst[1]) > int(lst[1]):
        tool = int(lst[0]) - int(lst[1])
    else:
        tool = int(lst[1])

    if int(lst[0]) - int(lst[2]) > int(lst[2]):
        arz = int(lst[0]) - int(lst[2])
    else:
        arz = int(lst[2])

print(tool * arz * 4)
