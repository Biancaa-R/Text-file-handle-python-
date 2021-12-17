#Python program to get information on a specific topic
import pywhatkit
searchvalue=input("Enter the text to search about it")
try:
    value=pywhatkit.info(searchvalue,10)
    print(value)
    print("Successfully searched")
    ch=input("Do you want to save this data?y/n")
    if ch in ("y","Y"):
        F=open("D:\\12th File handle\\Information.txt ","a")
        F.write(searchvalue,"\n")
        F.write(value,"\n")
        F.close()
        print("Data saved successfully")
except:
    print("Connection error")
    