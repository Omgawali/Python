#no is divisble by 5 or not

def divis(no):
    if(no%5==0):
        print("No is divisble by 5")
    else:
        print("Not divisible")    



def main():
    print("Enter a no")
    num=int(input())
    divis(num)

if __name__=="__main__":
    main()
