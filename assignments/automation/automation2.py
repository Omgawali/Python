from sys import *

def addition(No1,No2):
    ans=0
    ans=No1+No2
    return ans

def main():
    print("-------Automation script---------")

    print("Automation script name",argv[0])
    if(len(argv)==2):
        if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
            print("This automation script is used to perform addition of two num")
            exit()

        if(argv[1]=="-u" or argv[1]=="-U"):       #flag for displaying the usage of script
            print("Usage:Name_of_script first_argument second_argument")
            print("Example Demo.py 11 10")
            exit()
        else:
            print("There is no such option handle")    
    if(len(argv)!=3):
        print("Invalid number of argument")
        exit()
    else:
        ret=addition(int(argv[1]),int(argv[2])) 
        print("Addition is",ret)   
if __name__=="__main__":
    main()

#py automation1.py 11 10 