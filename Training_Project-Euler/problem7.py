"""
素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.
10 001 番目の素数を求めよ.

ans = [2]
for i in range(2, 50000):
    if i % 2 == 0:
        continue
    flag = True
    for j in range(2, i):
        if j % 2 == 0:
            continue
        if i % j ==0:
            flag = False
    if flag == True:
        ans.append(i)
#print(ans)
print(ans[10000])
"""
from sympy import prime
print(prime(10001))