


def ChkNum(no):
    if(no>0):
        print("It is Positive no")
    elif(no<0):
        print("It is negative no")
    else:
        print("Zero")



def main():
    print("Enter a no:")
    num=int(input())
    ChkNum(num)

if __name__=="__main__":
    main()