'''Write a function countmy( )in Python to read the text file
“Story.txt” and count the number of times “my” or “My” occurs in
the file.:'''

#Try using both read and readlines

def count_my(): #using read
    F=open("hi.txt","r")
    count=0
    value=F.read()
    line=value.split()

    for i in line:
        if i in ["my","My","MY"]:
            count+=1
    print("The total occurances of my is",count)


count_my()

def count_my2(): #using readlines
    F=open("hi.txt","r")
    count=0
    value=F.readlines()
    for line in value:
        line=line.split()
        for i in line:
            if i in ["my","My","MY"]:
                count+=1
    print("The total occurances of my is",count)


count_my2()
