def getSum(n):
    icnt=0
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        icnt=icnt+1
        n = n//10
       
    return icnt
   

    

def main():
    print("Enter a no")
    n=int(input())
    print(getSum(n))

if __name__=="__main__":
    main()