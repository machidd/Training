#左右どちらから読んでも同じ値になる数を回文数という.
#3桁の数の積で表される回文数の最大の数を求めよ

a = 999
b = 999

while a > 0:
    ans = str(a * b)
    length = len(ans)
    if length < 6:
        break
    #(ans[0]) == int(ans[5]) 
    if int(ans[1]) == int(ans[4]):
        print(ans)
    a -= 1
