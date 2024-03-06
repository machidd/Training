"""
問題1: 単語の検索
与えられた文字列から単語 "Python" を見つけてください。
"""

import re

given_text = "このテキストにはPythonという単語が含まれています。"
word = "Python"

print(re.search(word , given_text))