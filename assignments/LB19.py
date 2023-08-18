#count frequency of such digits which is less than 6 

def digfit(no):
    icnt=0

    while(no!=0):
        
        icnt=icnt+1
        no=no//10

    print(icnt)    




def main():
    print("enter a no ")
    num=int(input())
    digfit(num)

if __name__=="__main__":
    main()