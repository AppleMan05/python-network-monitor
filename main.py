import psutil
from plotting import plotting
from calculations import calculations

if __name__ == "__main__":
    time_asked = int(input("please send how long you want to monitor data. send value in seconds."))
    initial_down = psutil.net_io_counters().bytes_recv
    initial_up = psutil.net_io_counters().bytes_sent
    calculations(initial_up, initial_down, time_asked)
    