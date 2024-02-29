"""
最初の10個の自然数について, その二乗の和は,
12 + 22 + ... + 102 = 385

最初の10個の自然数について, その和の二乗は,
(1 + 2 + ... + 10)2 = 3025

これらの数の差は 3025 - 385 = 2640 となる.

同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
"""

wa = []
nijo = []

for i in range(1,101,1):
    wa.append(i)
wawa = sum(wa)
wawa = wawa * wawa

for i in range(1,101,1):
    a = i * i
    nijo.append(a)
nijowa = sum(nijo)

print(wawa - nijowa)