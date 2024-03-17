"""
解けているが計算量が終わっているので効率化の勉強する

三角数の数列は自然数の和で表され、7番目の三角数は1 + 2 + 3 + 4 + 5 + 6 + 7 = 28である
三角数の最初の10項は:
　1,3,6,10,15,21,28,36,45,55 ...
となる
最初の7項について、その約数を列挙すると、以下の通り
1:1
3:1,3
6:1,2,3,6
10:1,2,5,10
15:1,3,5,15
21:1,3,7,21
28:1,2,4,7,14,28
これから、7番目の三角数である28は5個より多く約数を持つ最初の三角数であることがわかる
では、500個より多く約数を持つ最初の三角数はいくつか
"""
a = 0
b = []
c = 0
ans = []
flag = True

max_num = 500
count = 0

while True:
    count += 1
    a += count
    ans = 0

    for i in range(a):
        if a % (i+1) == 0:
            ans += 1
    if ans > max_num:
        print(a)
        break

"""
while flag == True:
    for i in range(1, len(b)+1):
        if b[] % i == 0:
            ans.append(i)
            print(i)
        if len(ans) > 500:
            print(i)
            flag = False
print(len(ans))
"""
"""
for i in range(1,10):
    if int(b[c]) % i == 0:
        d.append(i)
    c += 1

print(d)
"""






"""
三角数を求める関数Aを作成
Aの数字について順に全ての約数を求め、listに追加
listのlen()が500に達したところで操作を中止しそのlistの数字を出力
"""