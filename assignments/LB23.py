
#return difference between summation of even an summation of odd

def evendi(no):
    icnt=0
    icnt1=0
    idigfiti=0
    while(no!=0):
        idigfiti=no%10
        if(no%2)==0:
            icnt=idigfiti+icnt
        elif(no%2)!=0:
            icnt1=idigfiti+icnt1    
        no=no//10
        

    print(icnt1-icnt)        
   

def main():
    print("enter a no")
    num=int(input())
    evendi(num)


if __name__=="__main__":
    main()