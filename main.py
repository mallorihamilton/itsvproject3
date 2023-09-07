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
for i in range(len(text)):
    text[i] = text[i][text[i].find("[")+1:text[i].find(":")]
print(len(text))
print(text)
