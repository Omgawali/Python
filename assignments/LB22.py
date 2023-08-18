#return multiplication of digits



def evendi(no):
    icnt=1
    idigfiti=0
    while(no!=0):
        idigfiti=no%10
        icnt=idigfiti*icnt
        no=no//10

    print(icnt)        
   

def main():
    print("enter a no")
    num=int(input())
    evendi(num)


if __name__=="__main__":
    main()