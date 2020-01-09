import re
pattern=re.compile(r'(^[a-zA-Z0-9_.+-]+@+[a-zA-Z0-9-]+\.+[a-zA-Z0-9-.]+$)')
string='rupakumari201@yahoo.com'
a=pattern.match(string)
print(a) #<re.Match object; span=(0, 23), match='rupakumari201@yahoo.com'>

