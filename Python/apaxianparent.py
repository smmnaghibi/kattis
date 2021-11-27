inp = input()
lst = inp.split()
if 2 <= len(lst[0]) <= 10 and 2 <= len(lst[1]) <= 10 and inp.islower():
    if lst[0][-1] == 'e':
        print(lst[0]+'x'+lst[1])
    elif lst[0][-1] == 'a' or lst[0][-1] == 'i' or lst[0][-1] == 'o' or lst[0][-1] == 'u':
        print(lst[0][:len(lst[0])-1] + 'ex' + lst[1])
    elif lst[0][-2:] == 'ex':
        print(lst[0]+lst[1])
    else:
        print(lst[0]+'ex'+lst[1])
