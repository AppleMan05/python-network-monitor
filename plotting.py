import matplotlib.pyplot as plt

def plotting(x,y,y1):
    plt.plot(x,y, label="Downloaded")
    plt.plot(x,y1,label="Uploaded")
    plt.xlabel("Time in seconds")
    plt.ylabel("Bandwidth used in MB")
    plt.title("bandwidth")
    plt.legend()
    plt.show()
    print(f'total upload = {up}, total download = {down}')

if __name__ == "__main__":
    print("Please run main.py")