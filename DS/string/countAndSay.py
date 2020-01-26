'''
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, …
How is above sequence generated?
n’th term in generated by reading (n-1)’th term.

The first term is "1"

Second term is "11", generated by reading first term as "One 1"
(There is one 1 in previous term)

Third term is "21", generated by reading second term as "Two 1"

Fourth term is "1211", generated by reading third term as "One 2 One 1"

and so on
'''


def countAndSay(self, n):
    # Base cases
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"
    s = "11"
    for i in range(3, n + 1):
        s += '$'
        l = len(s)

        cnt = 1
        tmp = ""

        for j in range(1, l):
            if (s[j] != s[j - 1]):
                tmp += str(cnt + 0)
                tmp += s[j - 1]
                cnt = 1
            else:
                cnt += 1

        s = tmp
    return s;

# Driver code
number = "1" # First member is always 1.
n = 6 # Number of members in the sequence
for i in range(n):
    print(number)
    number = countAndSay(number)