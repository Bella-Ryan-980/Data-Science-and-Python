import matplotlib.pyplot as plt
import numpy as np
import formatting as f

def Typical_Volume_By_Period_Graph_Gen ():
    x = []
    y = []
    size = []

    fileCheck = f.File_Check("Typical_Volume_By_Period_Type.csv")
    while fileCheck != False:
        with open("Typical_Volume_By_Period_Type.csv") as readFile:
            line = readFile.readline()
            while line:
                row = line.split(",")
                if row[0] != "Period_Type":
                    for i in range(23):
                        hour = i + 1
                        x.append(int(i))
                        y.append(row[0].rstrip())
                        size.append(int((row[hour].rstrip())[:-2]))
                line = readFile.readline()
        
        fig = plt.figure(figsize=(20, 5))
        ax = fig.add_subplot(1, 1, 1, aspect=1)
        ax.scatter(x, y, s=size, c="slateblue", alpha=0.3)
        plt.title("Typical Volume by Period")
        plt.xlabel("Hour of Day")
        plt.ylabel("Period")
        plt.xticks(np.arange(0, 24, step=1))
        plt.savefig("Typical_Volume_by_Period.png")
        break

def Typical_Volume_By_Flow_Graph_Gen ():
    x = []
    y = []
    size = []

    fileCheck = f.File_Check("Typical_Volume_By_Flow.csv")
    while fileCheck != False:
        with open("Typical_Volume_By_Flow.csv") as readFile:
            line = readFile.readline()
            while line:
                row = line.split(",")
                if row[0] != "Flow":
                    for i in range(23):
                        hour = i + 1
                        x.append(int(i))
                        y.append(row[0].rstrip())
                        size.append(int((row[hour].rstrip())[:-2]))
                line = readFile.readline()

        fig = plt.figure(figsize=(20, 5))
        ax = fig.add_subplot(1, 1, 1, aspect=1)
        ax.scatter(x, y, s=size, c="slateblue", alpha=0.3)
        plt.title("Typical Volume by Flow")
        plt.xlabel("Hour of Day")
        plt.ylabel("Flow")
        plt.xticks(np.arange(0, 24, step=1))
        plt.savefig("Typical_Volume_by_Flow.png")
        break
