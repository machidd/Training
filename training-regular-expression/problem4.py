"""
解けたけど正規表現の内容が完璧でない
問題4: HTMLタグの除去
与えられたHTML文字列から全てのHTMLタグを除去してください。
"""
import re

given_text = "<html><head><title>タイトル</title></head><body>この部分が本文です。</body></html>"
word = r"<.*?>"
print(re.sub(word ,"" ,given_text))