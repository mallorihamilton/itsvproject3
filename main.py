from urllib.request import urlretrieve
from datetime import datetime

import os.path
#Downloading the file
if(not os.path.isfile("Server Logs.csv")):
    url = ("https://s3.amazonaws.com/tcmg476/http_access_log")
    filename = "Server Logs.csv"
    urlretrieve(url, filename)

#Opening the file and reading the text from it
file = open("Server Logs.csv","r+")
txt = file.read()
text = txt.split("\n")
file.close()

oct1994 = open("October 1994.csv", "w+")
nov1994 = open("November 1994.csv", "w+")
dec1994 = open("December 1994.csv", "w+")
jan1995 = open("January 1995.csv", "w+")
feb1995 = open("February 1995.csv", "w+")
mar1995 = open("March 1995.csv", "w+")
apr1995 = open("April 1995.csv", "w+")
may1995 = open("May 1995.csv", "w+")
jun1995 = open("June 1995.csv", "w+")
jul1995 = open("July 1995.csv", "w+")
aug1995 = open("August 1995.csv", "w+")
sep1995 = open("September 1995.csv", "w+")
oct1995 = open("October 1995.csv", "w+")
increment = False
days = 0
redirected = 0
failed = 0
files = {}
highest = 0
high = ""
lowest = float('inf')
low = ""
dates = {}
sum = 0

oct4 = 0
nov4 = 0
dec4 = 0
jan5 = 0
feb5 = 0
mar5 = 0
apr5 = 0
may5 = 0
jun5 = 0
jul5 = 0
aug5 = 0
sep5 = 0
oct5 = 0

for i in range(len(text)):
    if "11/Apr/1995" in text[i]:
        increment = True
    if increment:
        days += 1
    
    if "Oct/1994" in text[i]:
        oct1994.write(text[i] + "\n")
        oct4 += 1
    elif "Nov/1994" in text[i]:
        nov1994.write(text[i] + "\n")
        nov4 += 1
    elif "Dec/1994" in text[i]:
        dec1994.write(text[i] + "\n")
        dec4 += 1
    elif "Jan/1995" in text[i]:
        jan1995.write(text[i] + "\n")
        jan5 += 1
    elif "Feb/1995" in text[i]:
        feb1995.write(text[i] + "\n")
        feb5 += 1
    elif "Mar/1995" in text[i]:
        mar1995.write(text[i] + "\n")
        mar5 += 1
    elif "Apr/1995" in text[i]:
        apr1995.write(text[i] + "\n")
        apr5 += 1
    elif "May/1995" in text[i]:
        may1995.write(text[i] + "\n")
        may5 += 1
    elif "Jun/1995" in text[i]:
        jun1995.write(text[i] + "\n")
        jun5 += 1
    elif "Jul/1995" in text[i]:
        jul1995.write(text[i] + "\n")
        jul5 += 1
    elif "Aug/1995" in text[i]:
        aug1995.write(text[i] + "\n")
        aug5 += 1
    elif "Sep/1995" in text[i]:
        sep1995.write(text[i] + "\n")
        sep5 += 1
    elif "Oct/1995" in text[i]:
        oct1995.write(text[i] + "\n")
        oct5 += 1
    text[i] = text[i].split(" ")
    
    if len(text[i]) == 10:
        if (int(int(text[i][8]) / 100)) == 4:
            failed += 1
        elif (int(int(text[i][8]) / 100)) == 3:
            redirected += 1
    
        if text[i][6] not in files:
            files.update({text[i][6]: 1})
        else:
            files.update({text[i][6]: files[text[i][6]] + 1})

        if text[i][3][1:12] not in dates:
            dates.update({text[i][3][1:12]: 1})
        else:
            dates.update({text[i][3][1:12]: dates[text[i][3][1:12]] + 1})


for item in files:
    if files[item] > highest:
        highest = files[item]
        high = item
    if files[item] < lowest:
        lowest = files[item]
        low = item

print(len(text), "total requests made in the time period.")
print(days, "requests made in the last 6 months.")

#Prints the number of requests on each day, but probably not what is being asked
for date in dates:
    print(dates[date], "requests were made on", date)

dailyRequests = float(len(text)) / len(dates)
print(dailyRequests, "requests were made each day on average.")
print(dailyRequests * 7, "requests were made each week on average.")

#Prints the number of requests on each month, but probably not what is being asked
print(oct4, "requests were made in October 1994.")
print(nov4, "requests were made in November 1994.")
print(dec4, "requests were made in December 1994.")
print(jan5, "requests were made in January 1995.")
print(feb5, "requests were made in February 1995.")
print(mar5, "requests were made in March 1995.")
print(apr5, "requests were made in April 1995.")
print(may5, "requests were made in May 1995.")
print(jun5, "requests were made in June 1995.")
print(jul5, "requests were made in July 1995.")
print(aug5, "requests were made in August 1995.")
print(sep5, "requests were made in September 1995.")
print(oct5, "requests were made in October 1995.")
print(float(oct4 + nov4 + dec4 + jan5 + feb5 + mar5 + apr5 + may5 + jun5 + jul5 + aug5 + sep5 + oct5) / 13, "requests were made each month on average.")

print(str(float(failed) / len(text)) + "% of the requests failed.")
print(str(float(redirected) / len(text)) + "% of the requests were redirected.")
print(high, "was the most requested file with", highest, "requests.")
print(low, "was the least-requested file with", lowest, "requests.")

oct1994.close()
nov1994.close()
dec1994.close()
jan1995.close()
feb1995.close()
mar1995.close()
apr1995.close()
may1995.close()
jun1995.close()
jul1995.close()
aug1995.close()
sep1995.close()
oct1995.close()

#Editing the text from the file
j = 0
increment = False
for i in range(len(text)):
    text[i] = text[i][text[i].find("[")+1:text[i].find(":")]
    if text[i] == "11/Apr/1995":
        increment = True
    if increment:
        j += 1
print(len(text), " total requests made in the time period")
#print(text)
print(j, " requests made in the last 6 months")