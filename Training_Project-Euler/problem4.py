#左右どちらから読んでも同じ値になる数を回文数という.
#3桁の数の積で表される回文数の最大の数を求めよ

a = 999
b = 999
c = []
while b > 99:
    while a > 99:
        ans = str(a * b)
        rev_ans = ans[::-1]
        if ans == rev_ans:
            c.append(int(ans))
            break
        else:
            a -= 1
    a = 999
    b -= 1

c.sort(reverse=True)
print(c[0])