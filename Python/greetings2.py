s = input()
if 3 <= len(s) <= 1000:
    count = s.count("e")
    res = "h{}y"
    print(res.format(2*count*"e"))
