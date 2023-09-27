from sys import *
import os
import time
def DirectoryTravel(Dirname):
    print("We are going to scan the directory ",Dirname)

    for foldername,subfoldername,filename in os.walk(Dirname):
        print("Current directory name",foldername)
        
        for subname in subfoldername:
            print("current sub",subname)
                        
        for fname in filename:
            print(fname,":",os.path.getsize(foldername+"/"+fname),"bytes")
            

def main():
    print("-------Automation script---------")
    
    print("Automation script name",argv[0])
    if(len(argv)!=2):
        print("Invalid number of argument")
        exit()
    else:
        pass
    if(len(argv)==2):
        if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
            print("This automation script is used to perform file automation")
            exit()

        if(argv[1]=="-u" or argv[1]=="-U"):       #flag for displaying the usage of script
            print("Usage:Name_of_script first_argument ")
            print("Example Demo.py marvellous")
            exit()
        else:
            starttime=time.time()
            DirectoryTravel(argv[1])
            endtime=time.time()

            print("",endtime-starttime)


if __name__=="__main__":
    main()

#py automation1.py directoryname