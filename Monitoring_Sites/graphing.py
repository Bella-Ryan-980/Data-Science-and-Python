import matplotlib.pyplot as plt
import formatting as f

def Monitoring_Pie ():
    fileCheck = f.File_Check("Monitoring_Type_Frequency.csv")

    labels = []
    sizes = []

    while fileCheck != False:
        with open("Monitoring_Type_Frequency.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Monitoring Type":
                    labels.append(row[0])
                    sizes.append(row[1])
                line = readFile.readline()
        break

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig("Monitoring_Type_Frequency_Plot.png")

def Site_Pie ():
    fileCheck = f.File_Check("Site_Frequency.csv")

    labels = []
    sizes = []
    d = {"other" : 0}

    while fileCheck != False:
        with open("Site_Frequency.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Site":
                    if int(row[1]) >= 9:
                        labels.append(row[0])
                        sizes.append(row[1])
                    else:
                        d["other"] +=1
                line = readFile.readline()
            labels.append("other")
            sizes.append(d["other"])
        break

    fig = plt.figure(figsize=(50, 50))
    ax = plt.subplots()
    ax.pie(sizes, autopct='%1.1f%%',shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(labels, loc = "best") 
    plt.savefig("Site_Frequency_Plot.png")

def Alpha_Pie ():
    fileCheck = f.File_Check("Site_Alpha_Frequency.csv")

    labels = []
    sizes = []
    d = {"other" : 0}

    while fileCheck != False:
        with open("Site_Alpha_Frequency.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Site Alpha":
                    if int(row[1]) >= 16:
                        labels.append(row[0])
                        sizes.append(row[1])
                    else:
                        d["other"] +=1
                line = readFile.readline()
            labels.append("other")
            sizes.append(d["other"])
        break

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig("Site_Alpha_Frequency_Plot.png")