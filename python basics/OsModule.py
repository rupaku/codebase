'''Os module'''
import os
print(os.name) #nt
print(os.getcwd()) #get current working dir
print(os.popen())#opens a pipe to ot from a cmd

#But file opened through os.popen(), can be closed with close() or
# os.close(). If we try closing a file opened with open(), using os.close(),
# Python would throw TypeError
print(os.close())

#os.rename()
import os
fd = "GFG.txt"
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')

