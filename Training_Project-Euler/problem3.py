#13195 の素因数は 5, 7, 13, 29 である.

#600851475143 の素因数のうち最大のものを求めよ.

number = 600851475143
prime_factors_dict = sympy.factorint(number)
print("素因数分解:", prime_factors_dict)
