import psutil
from sys import *
def ProcessDisplay(po):
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            if pinfo['name']==po:
                listprocess.append(pinfo)

        except(psutil.NoSucProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("Process Monitor")
    po=argv[1]
    listprocess=ProcessDisplay(po)

    for elem in listprocess:
        print(elem)


if __name__=="__main__":
    main()