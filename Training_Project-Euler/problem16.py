"""
2の15乗 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.

同様にして, 2の1000乗 の各位の数字の和を求めよ.
"""
j = 0
ans = 0

for i in range(1,1001):
    j = 2 ** i

newj = str(j)

for i in range(len(newj)):
    ans += int(newj[i])

print(ans)

