#accept no from user and return summation all non factors


def func(no):
    iCnt=1
    for i in range(no,0,-1):
        if ((no%i!=0)):
            
            iCnt=iCnt+i

    print(iCnt)        
           

def main():
    print("Enter a no ")
    num=int(input())
    func(num)

if __name__=="__main__":
    main()
