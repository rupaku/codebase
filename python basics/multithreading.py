from threading import Thread
import threading
from time import sleep

def naturalno():
    print(threading.current_thread().getName(),"has started")
    sleep(2) #sleep for 2 sec
    for i in range(10):
        print(i)
    print(threading.current_thread().getName(), "has ended")

t1=Thread(target=naturalno())
t2=Thread(target=naturalno())
t1.start()
t2.start()

#Lock and semaphore
class flightReservation:
    l=lock()
    def __init__(self,ticket_left):
        self,ticket_left=ticket_left
    l.aquire()
    def buy(self,ticketRequested):
        pass
    l.release()
