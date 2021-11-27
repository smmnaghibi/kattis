num = input().split()
lst = []
dic = {}
if 0 < int(num[0]) <= 100 and 0 < int(num[1]) <= 100 and 0 < int(num[2]) <= 100 :
    inp = input()
    if "A" in inp and "B" in inp and "C" in inp:
        for i in num:
            lst.append(int(i))
lstr = sorted(lst)
dic["A"] = lstr[0]
dic["B"] = lstr[1]
dic["C"] = lstr[2]

for j in inp:
    print(dic[j],end=" ")
