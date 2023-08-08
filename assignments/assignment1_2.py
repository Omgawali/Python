

def ChkNum(no1):
    if(no1%2==0):
        print("even no is",no1)
    else:
        print("odd no is",no1)



    

def main():
    print("Enter a no ")
    no=int(input())
    ChkNum(no)

if __name__=="__main__":
    main()
