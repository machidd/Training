"""
雑な指定をしたい時の正規表現方法がわからない
問題8: URLの検出
与えられた文字列からURLを全て検出してください。URLは、httpまたはhttpsで始まるものとします。
"""
import re

given_text = "参考になるウェブサイトはhttps://www.example.comとhttp://www.example.orgです。"
word = r"https*:\/\/[\w+.\w+.+]"
print(re.findall(word ,given_text))