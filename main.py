from urllib.request import urlretrieve
#Downloading the file
url = ("https://s3.amazonaws.com/tcmg476/http_access_log")
filename = "Server Logs.csv"
urlretrieve(url, filename)

#Opening the file and reading the text from it
file = open("Server Logs.csv","r+")
txt = file.read()
text = txt.split("\n")
#print(text)
file.close()

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