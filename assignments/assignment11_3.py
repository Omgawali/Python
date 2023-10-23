from sys import *
import os
import hashlib
import time

def hashfile(path,blocksize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()  

def findDuplicate(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    exist=os.path.isdir(path)
    dups={}
    if exist:
        for dirName,subdirs,filelist in os.walk(path):
            for filen in filelist:
                path=os.path.join(dirName,filen)
                file_hash=hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    log_dir="marvellous"
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator="-"*80
    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(time.time()))
    f = open(log_path,'w')
    f.write(seperator+"\n")
    f.write("Marvellous Infosystem Process Logger:"+time.ctime()+"\n")
    f.write(seperator+"\n")      

    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates found")
        print("the following files are identical")
        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    
                    f.write("%s\n" % subresult)
                    os.remove(subresult)


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
            exit()
    try:
        arr={}
        arr=findDuplicate(argv[1])
        PrintDuplicate(arr) 
    except ValueError:
        print("Invalid error")           

if __name__=="__main__":
    main()