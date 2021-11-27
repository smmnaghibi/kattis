n = int(input())
if 1 <= n <= 1000000000:
    nb = str(bin(n))
    x = nb[2::]
    print(int(x[::-1],2))
