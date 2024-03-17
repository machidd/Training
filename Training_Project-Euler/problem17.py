"""
1 から 5 までの数字を英単語で書けば one, two, three, four, five であり, 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.

では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.

注: 空白文字やハイフンを数えないこと. 例えば, 342 (three hundred and forty-two) は 23 文字, 115 (one hundred and fifteen) は20文字と数える. なお, "and" を使用するのは英国の慣習.
"""

ans = 0

def numsplit(num):
    ones_place = num % 10
    tens_place = (num // 10) * 10
    return tens_place, ones_place

def numsplit_overhundred(num):
    hundreds_place = num // 100
    return hundreds_place

numberdict = {0:"",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",
              12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty",40:"forty",50:"fifty",
              60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

for i in range(1,1000):
    if i in numberdict:
        ans += len(numberdict[i])
    elif i > 99:
        hundreds_place = numsplit_overhundred(i)
        if i % 100 == 0:
            """
            print(str(numberdict[hundreds_place]) + "hundred")
            """
            ans += len(numberdict[hundreds_place]) + 7
        else:
            x = i % 100
            if x in numberdict:
                """
                print(str(numberdict[hundreds_place]) + "hundred" + " and " + str(numberdict[x]))
                """
                ans += len(numberdict[hundreds_place]) + 10 + len(numberdict[x])
            else:
                tens_place, ones_place = numsplit(x)
                """
                print(str(numberdict[hundreds_place]) + "hundred" + " and " + str(numberdict[int(tens_place)]) + str(numberdict[int(ones_place)]))
                """
                ans += len(numberdict[hundreds_place]) + 10 + len(numberdict[int(tens_place)]) + len(numberdict[int(ones_place)])
    else:
        tens_place, ones_place = numsplit(i)
        """
        print(str(numberdict[int(tens_place)]) + str(numberdict[int(ones_place)]))
        """
        ans += len(numberdict[int(tens_place)]) + len(numberdict[int(ones_place)])

print(ans + 11)