def longlines():
    F=open("D:\\12th file handle\\story.txt","r")
    line=F.readlines()

    for i in line:
        if len(i)<50:
            print(i,end="   ")
            
    F.close()
longlines()     
