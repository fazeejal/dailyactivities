import threading
import time
def print_num():
    for i in range(6):
        time.sleep(1)
        print(f"thread1: {i}")
def print_letters():
    for l in 'ABCDE':
        time.sleep(1)
        print(f"thread2 :{l}")
##thread creation
thread1=threading.Thread(target=print_num)
thread2=threading.Thread(target=print_letters)
##start thread
thread1.start()
thread2.start()
