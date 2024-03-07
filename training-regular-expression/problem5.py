"""
解けた
問題5: IPアドレスの検出
与えられた文字列からIPv4アドレスを全て検出してください。
"""
import re

given_text = "このサーバーのIPアドレスは192.168.1.1です。別のアドレスとして10.0.0.1もあります。"
word = r"\d+.\d+.\d+.\d+"
ans = re.findall(word ,given_text)
print(ans)

