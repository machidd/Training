"""
解けた
問題7: 日付の抽出
与えられた文字列からYYYY/MM/DD形式の日付を全て抽出してください。
"""
import re

given_text = "前回の更新日は2023/04/15で、次の予定日は2023/05/20です。"

word = r"\d+\/\d+\/\d+"
ans = re.findall(word ,given_text)
print(ans)
