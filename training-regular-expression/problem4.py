"""
解けた
問題4: HTMLタグの除去
与えられたHTML文字列から全てのHTMLタグを除去してください。
"""
import re

given_text = "<html><head><title>タイトル</title></head><body>この部分が本文です。</body></html>"
print(re.sub(r"<.*?>" ,"" ,given_text))