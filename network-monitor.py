import psutil
from hurry.filesize import size
import time

time_asked = int(input("please send how long you want to monitor data. send value in seconds."))
initial_down = psutil.net_io_counters().bytes_recv
initial_up = psutil.net_io_counters().bytes_sent

time_done = 0

while time_done <= time_asked:
    up = size(psutil.net_io_counters().bytes_sent - initial_up)
    down = size(psutil.net_io_counters().bytes_recv - initial_down)
    print(f'uploaded = {up}, downloaded = {down}')
    time_done +=1
    time.sleep(1)

print(f'total upload = {up}, total download = {down}')

#print(f'downloaded={down}, uploaded={up}')

