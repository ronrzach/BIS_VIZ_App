import csv
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

print("Enter date in DD/MM/YYYY format and time in HH:MM:SS format \n")
sDate = input("Enter start date: ")
sTime = input("Enter start time: ")
eDate = input("Enter end date: ")
eTime = input("Enter end time: ")
bis_thresh = float(input("Enter BIS threshold value: "))
time_thresh = float(input("Enter Time threshold value: "))
x_plot_counter = 0.0
x_arr = []
y_arr = []
col_arr = []

with open("D:\CAREER\SCT HL7 Project\lbisThreshTest3.csv", "r", newline='') as csvf:
    csvR = csv.reader(csvf)
    flag = 5
    counter = 0
    event = 0

    for row in csvR:
        dnt_dropd = row[0]

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
            x_plot_counter = x_plot_counter + 1
            # print(float(row[1]),"\n")
            if float(row[1]) < bis_thresh:
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                counter = counter + 1
            elif float(row[1]) >= bis_thresh and counter < time_thresh:
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                counter = 0
            elif float(row[1]) >= bis_thresh and counter > time_thresh:
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                event = event + 1
                counter = 0


        elif flag == 0:
            x_plot_counter = x_plot_counter + 1
            # print(float(row[1]),"\n")
            if float(row[1]) < bis_thresh:
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                counter = counter + 1
            elif float(row[1]) >= bis_thresh and counter < time_thresh:
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                counter = 0
            elif float(row[1]) >= bis_thresh and counter > time_thresh:
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                event = event + 1
                counter = 0
            break

print("No of events: ", event)
x_arr = np.array(x_arr)
y_arr = np.array(y_arr)
plt.plot(x_arr, y_arr)
threshLine = np.array(list(50.0 for x in range(len(x_arr))))
plt.plot(x_arr, threshLine, linestyle = 'dotted')
plt.fill_between(x_arr, y_arr,color="red", where=(y_arr < bis_thresh))
plt.show()
csvf.close()