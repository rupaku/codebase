from threading import Thread
import threading
class myThread:
    def naturalno(self):
        for x in range(10):
            print(x)
obj=myThread()
t=Thread(target=obj.naturalno())
t.start()