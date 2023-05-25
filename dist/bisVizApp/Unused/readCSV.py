import csv

print("Enter date in DD/MM/YYYY format and time in HH:MM:SS format \n")
sDate = input("Enter start date: ")
sTime = input("Enter start time: ")
eDate = input("Enter end date: ")
eTime = input("Enter end time: ")

with open("D:\CAREER\SCT HL7 Project\hlbisCSV.csv", "r", newline='') as csvf:
    csvR = csv.reader(csvf)
    flag = 5
    for row in csvR:
        # print(row)
        if row == ['Time', 'AVGBIS']:
            continue

        rDT = row[0].split(" ")
        print(rDT[0], rDT[1])

        if rDT[0].strip() == sDate.strip() and rDT[1].strip() == sTime.strip():
            # print(rDT)
            flag = 1;
        if rDT[0].strip() == eDate.strip() and rDT[1].strip() == eTime.strip():
            # print(rDT)
            flag = 0;

        if flag == 1:
            print(row)

        elif flag == 0:
            print(row)
            break



csvf.close()