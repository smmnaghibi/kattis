inp = input()
lst = inp.split()

if 100 <= int(lst[0]) <= 999 and  100 <= int(lst[1]) <= 999 and int(lst[0]) != int(lst[1]) and "0" not in lst[0] and "0" not in lst[1]:
    num1 = str(lst[0])
    num2 = str(lst[1])
    print(max(int(num1[::-1]),int(num2[::-1])))
