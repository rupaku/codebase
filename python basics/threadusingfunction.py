''' thread
    any running program in computer is process
    any executing thing within process is thread
'''

from threading import Thread
import threading
def even():
    for x in range(20):
        if x%2 == 0:
            print(x)
    b = threading.current_thread().getName()
    print(b) #Thread-1 thread name

a= threading.current_thread().getName()
print(a) #MainThread  thread name
t=Thread(target=even)
t.start()