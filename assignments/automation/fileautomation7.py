from sys import *
import os
import time
def DirectoryTravel(Dirname):
    print("We are going to scan the directory ",Dirname)
    previos=0
    previosname=""

    flag=os.path.isabs(Dirname)
    if flag == False:
        Dirname=os.path.abspath(Dirname)

    exist=os.path.isdir(Dirname)

    if exist:    

        for foldername,subfoldername,filename in os.walk(Dirname):
            print("Current directory name",foldername)
                    
            for fname in filename:

                if (previos < os.path.getsize(os.path.join(foldername,fname))):
                    previos=os.path.getsize(os.path.join(foldername,fname))
                    previosname=os.path.join(foldername,fname)

        print("Maximum size",previos,previosname)
        os.remove(previosname)            

    else:
        print("Invalid path")        

def main():
    print("-------Automation script---------")
    
    print("Automation script name",argv[0])
   

    if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
        print("This automation script is used to perform file automation gfind a gfile in dir")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):       #flag for displaying the usage of script
        print("Usage:Name_of_script first_argument ")
        print("Example Demo.py marvellous ")
        exit()
    else:
        starttime=time.time()
        DirectoryTravel(argv[1])
        endtime=time.time()

        print("",endtime-starttime)


if __name__=="__main__":
    main()

#py automation1.py directoryname