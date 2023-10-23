
from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close
    return hasher.hexdigest()  

def DisplyChecksum(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exist=os.path.isdir(path)

    if exist:
        for Dirname,subdirs,filelist in os.walk(path):
            print("Current folder is"+Dirname)
            for filen in filelist:
                path=os.path.join(Dirname,filen)
                file_hash=hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
def main():

    if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
        print("This automation script is used to traverse specific directory")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):       #flag for displaying the usage of script
        print("Usage:Name_of_script first_argument ")
        print("Example Demo.py absolutepath_of_directory")
        exit()              

    try:
        arr=DisplyChecksum(argv[1])

    except ValueError:
        print("Error :Invalid datatype")
    except Exception:
         print("Error :Invalid Input")            

if __name__=="__main__":
    main()         