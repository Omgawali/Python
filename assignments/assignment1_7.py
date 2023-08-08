


def ChkNum(no):
    if(no%5==0):
        return True
        

def main():
    print("Enter a no:")
    num=int(input())
    no1=ChkNum(num)
    if(no1==True):
        print("true")
    else:
        print("false")    


if __name__=="__main__":
    main()
