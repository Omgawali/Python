import os
import psutil
import time
from sys import *
import os

import schedule

def ProcessDisplay(log_dir="Marvellous"):
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

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("Process Monitor")
    print("Automation script name",argv[0])
    
    
    
    schedule.every(1).minutes.do(ProcessDisplay(argv[1]))  # Run 'job' function every minute

while True:
    schedule.run_pending()  # Check and run pending tasks
    print("Checking for pending tasks...")
    time.sleep(1)

if __name__=="__main__":
    main()