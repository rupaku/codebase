''' reverse word
    'this is the best'
    o/p
    best the is this
    *remove all leading and trailing whitespace
'''

#method1
str='this is the best'
def reverse_word(str):
    return " ".join(reversed(str.split()))

#method2
def reverse_word(str):
    return " ".join(str.split()[::-1])

print(reverse_word(str))

#output
# best the is this

#method3
def reverse_word(str):
    words=[]
    length=len(str)
    spaces=[' ']
    i=0
    while i < length:
        if str[i] not in spaces:
            word_start=i
            while i < length  and str[i] not in spaces:
                i=i+1
            words.append(str[word_start:i])
        i=i+1
    return " ".join(reversed(words))

print(reverse_word(str))

#output
# best the is this