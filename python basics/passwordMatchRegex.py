import re
string='hdfbgd567hf$9'
pattern=re.compile(r"[a-zA-Z0-9!@#$]{8,'}\d") # {8,} atleast 8 char \d any digit
a=pattern.fullmatch(string)
print(a)