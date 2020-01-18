from collections import Counter
def anagram(s1,s2):
    return Counter(s1) == Counter(s2)

s1="cat"
s2="tac"
print(anagram(s1,s2)) #True