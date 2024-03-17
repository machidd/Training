"""
解けた
問題9: 数字のみを含む行の検出
与えられた複数行の文字列から、数字のみを含む行を全て検出してください。
"""
import re

given_text = "これはサンプルテキストです。\n12345\nテキストと数字123\n67890\n最後の行です。"

word = r"^[0-9]+"
print(re.findall(word, given_text, re.MULTILINE))