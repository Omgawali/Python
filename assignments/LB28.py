#Enter value
#4
#Enter values
#3
#*	*	*	
#*	*	*	
#*	*	*	
#*	*	*	

def pptr(no,no1):
    for i in range(1,no):
        
        for j in range(1,no1):
            print("*",end=" ")
        print("*")    


def main():
    print("Enter a no")
    num=int(input())
    print("Enter another no")
    num=int(input())

    pptr(num,num)

if __name__=="__main__":
    main()