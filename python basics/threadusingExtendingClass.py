from threading import Thread
import threading
class myThread(Thread):
    def run(self):
        print('hello')
        print(threading.current_thread().getName())
        for i in range(0,5):
            for j in range(i+1):
                print("*",end=" ")
            print("\r")

obj=myThread()
obj.start()

#output
# hello
# Thread-1
# *
# * *
# * * *
# * * * *
# * * * * *
