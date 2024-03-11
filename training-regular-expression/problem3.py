"""
解けた
問題3: 電話番号のフォーマット
与えられた10桁の電話番号（例: 1234567890）を、この形式（(123) 456-7890）にフォーマットしてください。
"""
import re

given_text = "1234567890"
ans1 = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", given_text)

print(ans1)


"""
"([1-9]{3}) [1-9]{3} - [1-9]{4}"
"""