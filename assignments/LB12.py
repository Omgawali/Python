#accept no from user and display multiply factor

def func(no):
    iCnt=1
    for i in range(1,no):
        if(no%i==0):
            iCnt=iCnt*i
            print(i)

    return iCnt        
    
def main():
    print("Enter a no")
    num=int(input())
    iNo=func(num)
    print(iNo)


if __name__=="__main__":
    main()