inp = input()
if 1 <= len(inp) <= 30 and inp.islower() and not inp.isspace():

    if "ss" in inp:
        print("hiss")
    else:
        print("no hiss")
