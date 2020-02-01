'''
1) Write a program that accepts multiple number of sentences as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect

Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
'''

def convert(input_str):
    return ''.join([chr(ord(char) - 32) for char in j if ord(char) >= 65])

if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        input_str = list(map(str,input().strip().split()))
        for j in input_str:
            print(convert(input_str),end=' ')



