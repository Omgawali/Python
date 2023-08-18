
def addoffac(no):
    isum=0
    for i in range(1,no):
        if(no%i==0):
            isum=isum+i 

    return isum         

def main():
    print("Enter a no :")
    num=int(input())

    ians=addoffac(num)
    print(ians)

if __name__=="__main__":
    main()