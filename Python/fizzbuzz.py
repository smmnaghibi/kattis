inp = input()
lst = inp.split()
if 1 <= int(lst[0]) < int(lst[1]) <= int(lst[2]) <= 100:
    for i in range(1,int(lst[2])+1):
        if i % int(lst[0]) == 0 and i % int(lst[1]) != 0:
            print("Fizz")
        elif i % int(lst[1]) == 0 and i % int(lst[0]) != 0:
            print("Buzz")
        elif i % int(lst[0]) == 0 and i % int(lst[1]) == 0:
            print("FizzBuzz")
        else:
            print(i)
