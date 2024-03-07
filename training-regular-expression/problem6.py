"""
解けた
与えられた文字列内の "Python" を "Julia" に置換してください。
"""
import re

given_text = "Pythonは素晴らしいプログラミング言語です。Pythonを学ぶことで多くのことができるようになります。"
word = r"Python"
print(re.sub(word , "Julia", given_text))