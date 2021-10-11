import psutil
from hurry.filesize import size
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


x = []
y = []
y1 =[]



time_asked = int(input("please send how long you want to monitor data. send value in seconds."))
initial_down = psutil.net_io_counters().bytes_recv
initial_up = psutil.net_io_counters().bytes_sent

time_done = 0

while time_done <= time_asked:
    up = int(psutil.net_io_counters().bytes_sent - initial_up)/1000000
    down = int(psutil.net_io_counters().bytes_recv - initial_down)/1000000
    
    print(f'uploaded = {up}, downloaded = {down}')
    y.append(down)
    y1.append(up)
    x.append(time_done)
    time_done +=1
    time.sleep(1)
    

plt.plot(x,y, label="Downloaded")
plt.plot(x,y1,label="Uploaded")
plt.xlabel("Time in seconds")
plt.ylabel("Bandwidth used in MB")
plt.title("bandwidth")
plt.legend()
plt.show()

print(f'total upload = {up}, total download = {down}')

#print(f'downloaded={down}, uploaded={up}')

