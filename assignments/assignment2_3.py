def fact(no):

    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact 

def main():
    print("Enter a no")
    num=int(input())

    ans=fact(num)
    print(ans)

if __name__=="__main__":
    main()