from sys import *
import os
def DirectoryTravel(Dirname):
    print("We are going to scan the directory ",Dirname)

    for foldername,subfoldername,filename in os.walk(Dirname):
        for fname in filename:
            print(fname)

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
            DirectoryTravel(argv[1])


if __name__=="__main__":
    main()

#py automation1.py directoryname