


    
def ChkNum(no):
    i=0
    while(i<no):
        if(i%2==0):
            print(i)
            i=i+1

        

def main():
    print("Enter a no:")
    num=int(input())
    ChkNum(num)
      


if __name__=="__main__":
    main()
