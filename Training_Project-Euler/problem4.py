#左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
#では, 3桁の数の積で表される回文数の最大値を求めよ.

a = 999
b = 999

while a > 0:
    ans = str(a * b)
    length = len(ans)
    if length < 6:
        break
    if int(ans[0]) == int(ans[5]):
        print(ans)
        print(length)
    a -= 1
    b -= 1
