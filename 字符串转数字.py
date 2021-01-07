s='31001301'
n = 31001301
newstr = s[::-1]
num = 0
for i, e in enumerate(newstr):
    # print(i,e)
    # i是坐标，e是元素
    for j in range(0, 10):
        if e == str(j):
            num = num + j*(10**i)

if num == n:
    print(num)