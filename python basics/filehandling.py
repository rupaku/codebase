''' file handling'''
#read
with open('file1.txt','r') as file:
    for each in file:
        print(each)


#readlines :to read multiple line

with open('file1.txt','r') as file:
    print(file.readlines())

#output
# ['Cool peoplenice env']


#write
file=open('file1.txt','r')
print(file.read()) # 1 line
print(file.read(5)) #5 character
file.close()

#write
with open('file1.txt','w') as file: #no need to close file in with
    file.write('Cool people')


#append
with open('file1.txt','a') as file:
    file.write('nice env')

#with statement
# using this method any files opened will be closed automatically after one is done, so auto-cleanup.

#split
with open('file1.txt','r') as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)

#output
# ['Cool', 'peoplenice', 'env']
