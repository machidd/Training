"""
次の情報が与えられている.

    1900年1月1日は月曜日である.
    9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
    2月は28日まであるが, うるう年のときは29日である.
    うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.

20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
"""
"""
日付を順にインクリメントする
曜日を月〜日で(0〜6?)周期で
日0 月1 火2 水3 木4 金5 土6

1900/1/1 = 1
1900/1/2 = 2
"""

ymd_num = [1900, 1, 1]
week_num = 1
count = 0

while True:
    week_num += 1
    ymd_num[2] += 1
    if week_num == 7:
        week_num = 0
    if ymd_num[1] == 2 and ymd_num[2] == 29:
        ymd_num[2] = 1
        ymd_num[1] += 1
    #31日ある月の条件
    if ymd_num[1] != 2 and ymd_num[1] != 4 and ymd_num[1] != 6 and ymd_num[1] != 9 and ymd_num[1] != 11 and ymd_num[2] == 32:
        ymd_num[2] = 1
        ymd_num[1] += 1
    #30日の月の条件
    if ymd_num[1] == 2 and ymd_num[2] == 29 and ymd_num[0] % 4 == 0 and ymd_num[0] % 100 == 0 and ymd_num[0] % 400 != 0:
        continue
    if ymd_num[1] == 2 and ymd_num[2] == 29:
        ymd_num[2] = 1
        ymd_num[1] += 1
    if ymd_num[1] == 4 and ymd_num[2] == 31:
        ymd_num[2] = 1
        ymd_num[1] += 1
    if ymd_num[1] == 6 and ymd_num[2] == 31:
        ymd_num[2] = 1
        ymd_num[1] += 1
    if ymd_num[1] == 9 and ymd_num[2] == 31:
        ymd_num[2] = 1
        ymd_num[1] += 1
    if ymd_num[1] == 11 and ymd_num[2] == 31:
        ymd_num[2] = 1
        ymd_num[1] += 1
    if ymd_num[1] == 13:
        ymd_num[0] += 1
        ymd_num[1] = 1
    if ymd_num[0] > 1900 and ymd_num[2] == 1 and week_num == 0:
        count += 1
    if ymd_num[0] == 2001:
        break
print(count)

"""
    print(str(ymd_num[0]) + "年" + str(ymd_num[1]) + "月" + str(ymd_num[2]) + "日です" + str(week_num) +" "+ str(count))
"""