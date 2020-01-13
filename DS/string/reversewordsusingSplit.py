def reverseword(s):
    words = s.split(' ')
    string = []
    for word in words:
        string.insert(0, word)
    print(" ".join(string))

s='i love programming'
reverseword(s)