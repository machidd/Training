#10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.
#同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.

A = 0
B = 0
C = 0

for i in range(1000):
    if i % 3 == 0:
        A += i
    if i % 5 == 0:
        B += i
    if i % 15 == 0:
        C -= i
print(A + B + C)