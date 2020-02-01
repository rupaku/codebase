import os


def findInsub(filename,subdirectory=''):
    if subdirectory:
        path=subdirectory
    else:
        path=os.getcwd()
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.join(root,filename)
    return None

print(findInsub('abc.txt', 'codebase\DS'))