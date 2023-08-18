#return the count of even digits

def evendi(no):
    icnt=0
    while(no!=0):
        if(no%2)==0:
            icnt+=1
        no=no//10

    print(icnt)        
   

def main():
    print("enter a no")
    num=int(input())
    evendi(num)




if __name__=="__main__":
    main()