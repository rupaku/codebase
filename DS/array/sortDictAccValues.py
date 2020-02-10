d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a = sorted(d.items(), key=lambda x: x[1])
print(a)

#output
#[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)]