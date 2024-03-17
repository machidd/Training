"""
2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある
では, 20×20 のマス目ではいくつのルートがあるか.
"""
import math

a = 20
b = 20
c = a + b

print(math.factorial(c) / math.factorial(b) / math.factorial(a))