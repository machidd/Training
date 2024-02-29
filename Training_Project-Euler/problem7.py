"""
素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.

10 001 番目の素数を求めよ.
"""

ans = []
for i in range(2, 10000):
    flag = True
    for j in range(2, i):
        if i % j ==0:
            flag = False
    if flag == True:
        ans.append(i)
print(ans)
#print(ans[1000])