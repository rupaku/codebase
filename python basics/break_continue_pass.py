''' break
    breaks thru loop and jumps to  next statement
'''

li=[1,2,3]
for i in li:
    print(i)
    break

#output
# 1

li=[1,2,3]
for i in li:
    print(i)
    continue

#output
# 1
# 2
# 3

''' pass'''
for i in [1,2]:
    pass

#exercise
pixel=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0]
]
for row in pixel:
    for image in row:
        if image == 1:
            print('*',end= ' ')
        else:
            print(' ',end=' ')
    print('')

#output
  #     *
  #   * * *
  # * * * * *
  #     *
