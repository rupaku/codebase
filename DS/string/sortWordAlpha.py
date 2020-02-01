'''
2) Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world
'''

s = list(map(str, input().split()))
emls = []
words= [i for i in s ]
for word in words:
    if word not in emls:
        emls.append(word)
# print(emls)
n=len(emls)
for i in range(n):
    for j in range(1,n-i):
        if emls[j] < emls[j-1]:
            (emls[j-1], emls[j]) = (emls[j], emls[j-1])
print(" ".join(emls))
