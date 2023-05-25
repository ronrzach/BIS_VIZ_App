import csv

print("Enter date in DD/MM/YYYY format and time in HH:MM:SS format \n")
sDate = input("Enter start date: ")
sTime = input("Enter start time: ")
eDate = input("Enter end date: ")
eTime = input("Enter end time: ")
bis_thresh = float(input("Enter BIS threshold value: "))
time_thresh = float(input("Enter Time threshold value: "))

with open("D:\CAREER\SCT HL7 Project\lbisThreshTest1.csv", "r", newline='') as csvf:
    csvR = csv.reader(csvf)
    flag = 5
    counter = 0
    event = 0
    for row in csvR:
        # print(row)
        if row == ['Time', 'AVGBIS']:
            continue

        rDT = row[0].split(" ")
        print(rDT[0], rDT[1])

        if rDT[0].strip() == sDate.strip() and rDT[1].strip() == sTime.strip():
            # print(rDT)
            flag = 1
        if rDT[0].strip() == eDate.strip() and rDT[1].strip() == eTime.strip():
            # print(rDT)
            flag = 0

        if flag == 1:
            # print(float(row[1]),"\n")
            if float(row[1]) < bis_thresh:
                counter = counter + 1
            elif float(row[1]) >= bis_thresh and counter < time_thresh:
                counter = 0
            elif float(row[1]) >= bis_thresh and counter > time_thresh:
                event = event + 1
                counter = 0


        elif flag == 0:
            break

print("No of events: ", event)

csvf.close()