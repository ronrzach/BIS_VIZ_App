spa = open("D:\CAREER\SCT HL7 Project\H11231513_SNB241927.spa", "r")
# print(spa.read())
l = len(spa.readline())
cont = spa.readlines()
dataList = []
idx = 0
# print(cont[1])

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

for i in range(l):
    dataList = cont[i].split("|")

    if(i == 0):
        print(dataList[0].strip(),"                  ",dataList[idx].strip())
    else:
        print(dataList[0].strip(), "   ", dataList[idx].strip())

