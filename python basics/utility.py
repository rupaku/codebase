''' utility function for unitest module'''
# def do_stuff(num):
#     try:
#         return int(num)+5
#     except ValueError as err:
#         return err

#No value in param
def do_stuff(num=0):
    try:
        if num:
            return int(num)+5
        else:
            return 'please enter a num'
    except ValueError as err:
        return err