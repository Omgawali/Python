#Enter value
#4
#Enter values
#3
#1	2	3	
#1	2	3	
#1	2	3	
#1	2	3

def pptr(no,no1):
    for i in range(no):
        icnt=0
        for j in range(no1):
            icnt=icnt+1
            print(icnt,end=" ")
        print()    


def main():
    print("Enter a no")
    num=int(input())
    print("Enter another no")
    num=int(input())

    pptr(num,num)

if __name__=="__main__":
    main()