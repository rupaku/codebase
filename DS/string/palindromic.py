'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''


def sentencePalindrome(s):
    l, h = 0, len(s) - 1

    # Lowercase string
    s = s.lower()

    # Compares character until they are equal
    while (l <= h):

        # If there is another symbol in left
        # of sentence
        if (not (s[l] >= 'a' and s[l] <= 'z')):
            l += 1

        # If there is another symbol in right
        # of sentence
        elif (not (s[h] >= 'a' and s[h] <= 'z')):
            h -= 1

        # If characters are equal
        elif (s[l] == s[h]):
            l += 1
            h -= 1

        # If characters are not equal then
        # sentence is not palindrome
        else:
            return False
    # Returns true if sentence is palindrome
    return True


# Driver program to test sentencePalindrome()
# s = "A man, a plan, a canal: Panama"
s="race a car"
if (sentencePalindrome(s)):
    print("Sentence is palindrome.")
else:
    print("Sentence is not palindrome.")

#method2
    import re
    def isPalindrome(A):
        if A == "":
            return 1

        A = re.sub('[^a-zA-Z0-9]', '', A)
        # if A == "":
        #     return 1

        A = A.lower()

        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] != A[j]:
                return 0
            i += 1
            j -= 1
        return 1