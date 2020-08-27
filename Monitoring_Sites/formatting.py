def File_Check (filename):
    try:
        file = open(filename, "r")
    except IOError:
        print (f"file does not exist")
        return False

def Monitoring_Formatting ():
    writeFile = open("Monitoring_Type_AND_Site_Name.csv", "w")
    writeFile.write("Monitoring Type,Site Name\n")

    fileCheck = File_Check("monitoring-sites-on-open-data.csv")
    while fileCheck != False:
        with open("monitoring-sites-on-open-data.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Monitoring type":
                    writeFile.write(f"{row[0]},{row[1]}\n")
                line = readFile.readline()
        break
    writeFile.close()

def Monitoring_Types_Frequency ():
    writeFile = open("Monitoring_Type_Frequency.csv", "w")
    writeFile.write("Monitoring Type,Frequency\n")

    d = {}

    fileCheck = File_Check("Monitoring_Type_AND_Site_Name.csv")
    while fileCheck != False:
        with open("Monitoring_Type_AND_Site_Name.csv", "r") as readFile:
            line = readFile.readline()  # get first line
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Monitoring Type":
                    if row[0] in d:
                        d[row[0]] += 1
                    else:
                        d[row[0]] = 1
                line = readFile.readline()  # get next line
            for key, value in d.items():
                writeFile.write(f"{key},{value}\n")
        break
    writeFile.close()

def Site_Frequency ():
    writeFile = open("Site_Frequency.csv", "w")
    writeFile.write("Site,Frequency\n")

    d = {}

    fileCheck = File_Check("Monitoring_Type_AND_Site_Name.csv")
    while fileCheck != False:
        with open("Monitoring_Type_AND_Site_Name.csv", "r") as readFile:
            line = readFile.readline()  # get first line
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[1] != "Site Name":
                    if row[1] in d:
                        d[row[1]] += 1
                    else:
                        d[row[1]] = 1
                line = readFile.readline()  # get next line
            for key, value in d.items():
                writeFile.write(f"{key},{value}\n")
        break
    writeFile.close()

def Site_Alpha_Frequency ():
    writeFile = open("Site_Alpha_Frequency.csv", "w")
    writeFile.write("Site Alpha,Frequency\n")

    d = {}

    fileCheck = File_Check("Monitoring_Type_AND_Site_Name.csv")
    while fileCheck != False:
        with open("Monitoring_Type_AND_Site_Name.csv", "r") as readFile:
            line = readFile.readline()  # get first line
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[1] != "Site Name":
                    if row[1][0] in d:
                        d[row[1][0]] += 1
                    else:
                        d[row[1][0]] = 1
                line = readFile.readline()  # get next line
            for key, value in d.items():
                writeFile.write(f"{key},{value}\n")
        break
    writeFile.close()