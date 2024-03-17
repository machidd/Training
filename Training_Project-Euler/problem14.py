"""
正の整数に以下の式で繰り返し生成する数列を定義する.

    n → n/2 (n が偶数)

    n → 3n + 1 (n が奇数)

13からはじめるとこの数列は以下のようになる.
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

13から1まで10個の項になる. この数列はどのような数字からはじめても最終的には 1 になると考えられているが, まだそのことは証明されていない(コラッツ問題)

さて, 100万未満の数字の中でどの数字からはじめれば最長の数列を生成するか.

注意: 数列の途中で100万以上になってもよい
"""
num = 13

def get_conrad(num):
    count = 0
    while True:
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        if num == 1:
            count += 1
            break
    return count

max_count = 0
max_num = 0
for i in range(2,1000000):
    conradcount = get_conrad(i)
    if conradcount > max_count:
        max_count = conradcount
        max_num = i
print(max_count, max_num)

"""
999999から操作を行う
"""