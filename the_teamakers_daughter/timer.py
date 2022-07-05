import threading
import os

def consequence():
    print('You took too long and the walls closed in on you')
    os._exit(os.EX_OK)
    #closes multiple-thread programs

s = threading.Timer(3.0, consequence())

s.start()
#as of this line, 3 seconds timer is running

