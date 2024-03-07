"""
問題2: メールアドレスの検出
与えられた文字列からメールアドレスを全て検出してください。メールアドレスは、一般的な形式（例: username@example.com）に従っているとします。
"""
import re

given_text = "連絡先はtaro@example.com、またはhanako@example.co.jpです。"

ans = re.findall(r"[a-z]+@example.[a-z.]+" , given_text)
print(ans)
