def anagram(s1,s2):
    d={}
    for i in s1,s2:
        d[i]={}
        for count in i:
            d[i][count]=d[i].get(count,0)+1
        return d[s1] == d[s2]

s1="cat"
s2="tac"
print(anagram(s1,s2))
