'''
Given s = "Hello World",

return 5 as length("World") = 5.
'''
def lengthLastWord(str):
    words = str.split(' ')
    for word in words:
        return len(word)

str="hello world   xDGBklKecz IAcOJYOH O  WY WPi"
print(lengthLastWord(str))

#method2
def lengthOfLastWord(a):
    count = 0
    x = a.strip()
    for i in range(len(x)):
        if x[i] == " ":
            count = 0
        else:
            count += 1
    return count


