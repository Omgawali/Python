from sys import *
import os
import time
import shutil
def DirectoryTravel(Dirname,Dirname1):
    print("We are going to scan the directory ",Dirname)

    flag=os.path.isabs(Dirname)
    if flag == False:
        Dirname=os.path.abspath(Dirname)

    exist=os.path.isdir(Dirname)

    if not os.path.exists(Dirname1):
        os.makedirs(Dirname1)

   

    for foldername,subfoldername,filename in os.walk(Dirname):
        print("Current directory name",foldername)
                    
        for fname in filename:
            src_path = os.path.join(foldername,fname)
            dest_path = os.path.join(Dirname1,  os.path.relpath(src_path, Dirname))
            
                
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} to {dest_path}")

     

def main():
    print("-------Automation script---------")
    
    print("Automation script name",argv[0])
   
    if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
        print("This automation script is used to perform file automation gfind a gfile withextetionin diradchjagfeextetio")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):       #flag for displaying the usage of script
        print("Usage:Name_of_script first_argument Second_argument ")
        print("Example Demo.py marvellous demo.txt")
        exit()
    else:
        starttime=time.time()
        DirectoryTravel(argv[1],argv[2])
        endtime=time.time()

        print("",endtime-starttime)


if __name__=="__main__":
    main()            