inp = input().split()
if len(inp[0]) == 3 and inp[0].isupper() and 1 <= int(inp[1]) <= 31:
    if (inp[0] == "OCT" and inp[1] == "31") or (inp[0] == "DEC" and inp[1] == "25"):
        print("yup")
    else:
        print("nope")
