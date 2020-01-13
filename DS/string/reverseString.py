#using loop
def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
print(reverse('abc')) #cba

#using recursion

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:])+s[0]

print(reverse('abc')) #cba

#using slicing
# b=a[::-1]