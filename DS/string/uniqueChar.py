''' unique char in string'''
def unique_char(str):
    return len(set(str)) == len(str)

print(unique_char('abcdea')) #False
print(unique_char('abcd')) #True

#method2
def unique_char(str):
    chars=set()
    for i in str:
        if i in chars:
            return False
        else:
            chars.add(i)
    return True

print(unique_char('abcd')) #True