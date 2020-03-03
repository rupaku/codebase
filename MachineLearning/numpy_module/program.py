import numpy as np
arr=np.arange(0,11)
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])

arr[1:5] #array([1, 2, 3, 4])

arr_copy=arr.copy()
arr_copy #array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr_2d=np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d
#array([[ 5, 10, 15],
#       [20, 25, 30],
#       [35, 40, 45]])

arr_2d[2][1] #40
arr_2d[2,1] #40

arr_2d[:2,1:]
#array([[10, 15],
#       [25, 30]])


arr=np.arange(1,11)
arr #array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

bool_arr=arr >3
bool_arr
#array([False, False, False,  True,  True,  True,  True,  True,  True,
#        True])

