#フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#数列の項の値が400万以下のとき, 値が偶数の項の総和を求めよ.


list = []

a, b = 1, 1
while b < 4000000:
    a, b = b, a+b
    if b % 2 == 0:
        list.append(b)
print(list)
Answer = sum(list)
print(Answer)