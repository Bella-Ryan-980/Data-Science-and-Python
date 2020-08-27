def File_Check (filename):
    try:
        file = open(filename, "r")
    except IOError:
        print (f"file does not exist")
        return False

def Link_ID_Desc ():
    writeFile = open("Link_ID_Desc.csv", "w")
    writeFile.write("Link_ID,Link_Desc\n")

    d = {}

    fileCheck = File_Check("TYPICAL_HOURLY_VOLUME_DATA.csv")
    while fileCheck != False:
        with open("TYPICAL_HOURLY_VOLUME_DATA.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[1] != "HMGNS_LNK_ID" and row[2] != "":
                    if row[1] not in d:
                        d[row[1]] = row[2]
                line = readFile.readline()
            for key, value in d.items():
                writeFile.write(f"{key},{value}\n")
        break
    writeFile.close()

def Typical_Volume_Data_Format ():
    writeFile = open("Typical_Volume_Data.csv", "w")
    writeFile.write("Link_ID,Flow_Direction,Period_Type,Hour_0,Hour_1,Hour_2,Hour_3,Hour_4,Hour_5,Hour_6,Hour_7,Hour_8,Hour_9,Hour_10,Hour_11,Hour_12,Hour_13,Hour_14,Hour_15,Hour_16,Hour_17,Hour_18,Hour_19,Hour_20,Hour_21,Hour_22,Hour_23\n")


    fileCheck = File_Check("TYPICAL_HOURLY_VOLUME_DATA.csv")
    while fileCheck != False:
        with open("TYPICAL_HOURLY_VOLUME_DATA.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[1] != "HMGNS_LNK_ID" and row[2] != "":
                    writeFile.write(f"{row[1]},{row[3]},{row[6]},{row[7]},{row[8]},{row[9]},{row[10]},{row[11]},{row[12]},{row[13]},{row[14]},{row[15]},{row[16]},{row[17]},{row[18]},{row[19]},{row[20]},{row[21]},{row[22]},{row[23]},{row[24]},{row[25]},{row[26]},{row[27]},{row[28]},{row[29]},{row[30]}\n")
                line = readFile.readline()
        break
    writeFile.close()

def Typical_Volume_By_Period_Type ():
    writeFile = open("Typical_Volume_By_Period_Type.csv", "w")
    writeFile.write("Period_Type,Hour_0,Hour_1,Hour_2,Hour_3,Hour_4,Hour_5,Hour_6,Hour_7,Hour_8,Hour_9,Hour_10,Hour_11,Hour_12,Hour_13,Hour_14,Hour_15,Hour_16,Hour_17,Hour_18,Hour_19,Hour_20,Hour_21,Hour_22,Hour_23\n")

    d = {}

    fileCheck = File_Check("Typical_Volume_Data.csv")
    while fileCheck != False:
        with open("Typical_Volume_Data.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Link_ID":
                    if row[2] not in d:
                        d[row[2]] = [1, int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]), int(row[16]), int(row[17]), int(row[18]), int(row[19]), int(row[20]), int(row[21]), int(row[22]), int(row[23]), int(row[24]), int(row[25]), int(row[26])]
                    else:
                        d[row[2]][0] += 1
                        for i in range(24):
                            item = i + 1
                            hour = i + 3
                            d[row[2]][item] += int(row[hour])
                line = readFile.readline()
            for key, value in d.items():
                writeFile.write(f"{key},{round(value[1]/value[0], 0)},{round(value[2]/value[0], 0)},{round(value[3]/value[0], 0)},{round(value[4]/value[0], 0)},{round(value[5]/value[0], 0)},{round(value[6]/value[0], 0)},{round(value[7]/value[0], 0)},{round(value[8]/value[0], 0)},{round(value[9]/value[10], 0)},{round(value[1]/value[11], 0)},{round(value[1]/value[12], 0)},{round(value[13]/value[0], 0)},{round(value[14]/value[0], 0)},{round(value[15]/value[0], 0)},{round(value[16]/value[0], 0)},{round(value[17]/value[0], 0)},{round(value[18]/value[0], 0)},{round(value[19]/value[0], 0)},{round(value[20]/value[0], 0)},{round(value[21]/value[0], 0)},{round(value[22]/value[0], 0)},{round(value[23]/value[0], 0)},{round(value[24]/value[0], 0)}\n")
            break

def Typical_Volume_By_Flow ():
    writeFile = open("Typical_Volume_By_Flow.csv", "w")
    writeFile.write("Flow,Hour_0,Hour_1,Hour_2,Hour_3,Hour_4,Hour_5,Hour_6,Hour_7,Hour_8,Hour_9,Hour_10,Hour_11,Hour_12,Hour_13,Hour_14,Hour_15,Hour_16,Hour_17,Hour_18,Hour_19,Hour_20,Hour_21,Hour_22,Hour_23\n")

    d = {}

    fileCheck = File_Check("Typical_Volume_Data.csv")
    while fileCheck != False:
        with open("Typical_Volume_Data.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Link_ID":
                    if row[1] not in d:
                        d[row[1]] = [1, int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]), int(row[16]), int(row[17]), int(row[18]), int(row[19]), int(row[20]), int(row[21]), int(row[22]), int(row[23]), int(row[24]), int(row[25]), int(row[26])]
                    else:
                        d[row[1]][0] += 1
                        for i in range(24):
                            item = i + 1
                            hour = i + 3
                            d[row[1]][item] += int(row[hour])
                line = readFile.readline()
            for key, value in d.items():
                writeFile.write(f"{key},{round(value[1]/value[0], 0)},{round(value[2]/value[0], 0)},{round(value[3]/value[0], 0)},{round(value[4]/value[0], 0)},{round(value[5]/value[0], 0)},{round(value[6]/value[0], 0)},{round(value[7]/value[0], 0)},{round(value[8]/value[0], 0)},{round(value[9]/value[10], 0)},{round(value[1]/value[11], 0)},{round(value[1]/value[12], 0)},{round(value[13]/value[0], 0)},{round(value[14]/value[0], 0)},{round(value[15]/value[0], 0)},{round(value[16]/value[0], 0)},{round(value[17]/value[0], 0)},{round(value[18]/value[0], 0)},{round(value[19]/value[0], 0)},{round(value[20]/value[0], 0)},{round(value[21]/value[0], 0)},{round(value[22]/value[0], 0)},{round(value[23]/value[0], 0)},{round(value[24]/value[0], 0)}\n")
            break

def Total_Volume_By_Flow ():
    writeFile = open("Total_Volume_By_Flow.csv", "w")
    writeFile.write("Flow,Total\n")

    d = {}

    fileCheck = File_Check("Typical_Volume_Data.csv")
    while fileCheck != False:
        with open("Typical_Volume_Data.csv", "r") as readFile:
            line = readFile.readline()
            while line:
                line = line.rstrip()
                row = line.split(",")
                if row[0] != "Link_ID":
                    if row[1] not in d:
                        d[row[1]] = 0
                        for i in range(24):
                            item = i + 3
                            d[row[1]] += int(row[item])
                    else:
                        for i in range(24):
                            item = i +3
                            d[row[1]] += int(row[item])
                line = readFile.readline()
            for key, value in d.items():
                writeFile.write(f"{key},{value}\n")
            break
