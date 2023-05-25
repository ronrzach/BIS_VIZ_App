import csv
import datetime

# print("Enter date in DD/MM/YYYY format and time in HH:MM:SS format \n")
# sdate = input("Enter start date: ")
#
# stime = input("Enter start time: ")
# edate = input("Enter end date: ")
# etime = input("Enter end time: ")

print(datetime.date())

spa = open("D:\CAREER\SCT HL7 Project\H11231513_SNB241927.spa", "r")
# print(spa.read())
l = len(spa.readline())
cont = spa.readlines()
dataList = []
idx = 0

# To find index of "AVGBIS"

for i in range(l):
    if i == 1:
        continue
    elif i == 0:
        dataList = cont[i].split("|")
        for j in range(len(dataList)):
            if dataList[j].strip() == "AVGBIS":
                idx = j;
                break
        else:
            continue
        break
    else:
        continue


# To transfer values to CSV file

with open("D:\CAREER\SCT HL7 Project\hlbisCSVcopy.csv", "w", newline='') as csvf:
    hList = ["Time","AVGBIS"]
    csvW = csv.DictWriter(csvf, fieldnames=hList)
    csvW.writeheader()

    for i in range(l):
        dataList = cont[i].split("|")

        if (i>0):
            val = float(dataList[idx].strip())
        csvrow = []

        # if(i<1):
        #     hList.append(dataList[0].strip())
        #     hList.append(dataList[idx].strip())

        elif(i > 0 and val <= 100):
            csvrow.append(dataList[0].strip())
            csvrow.append(dataList[idx].strip())
            csvW.writerow(csvrow)
        else:
            continue
csvf.close()




