"""
n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.

例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.

では, 100! の各位の数字の和を求めよ.
"""

num = 100
val = 1
ans = 0

for i in range(num, 1, -1):
    val *= i

newval = str(val)

for i in range(len(newval)):
   ans += int(newval[i]) 

print(ans)