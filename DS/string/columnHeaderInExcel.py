# 1 - A
# 2 - B
# ..
# 26 - Z
# 27 - AA
# ..
# 701 - ZY
# 706 - AAD
#
# A..Z, AA..ZZ, AAA..ZZZ, ….
def convertToBase(n):
    str ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base_num = 26
    start = n - 1  # n=26 ,start=25
    if start < base_num:
        return str[start]  # str[25] : Z
    else:
        return convertToBase(start // base_num) + str[start % base_num]
# n=27 start=26 base_num=26 func(26//26) func(1) ‘A’
# str[26 % 26] -> str[0]  ‘A’

print(convertToBase(27))
