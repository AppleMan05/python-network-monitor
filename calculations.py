import plotting
import time
import psutil
from plotting import plotting
def calculations(initial_up, initial_down, time_asked):
    time_done = 0
    x=[]
    y=[]
    y1=[]
    while time_done <= time_asked:
        up = int(psutil.net_io_counters().bytes_sent - initial_up)/1000000
        down = int(psutil.net_io_counters().bytes_recv - initial_down)/1000000
        y.append(down)
        y1.append(up)
        x.append(time_done)
        time_done+=1
        print(f'uploaded = {up}, downloaded = {down}')
        time.sleep(1)
    plotting(x, y, y1)

if __name__ == "__main__":
    print("Please run main.py")