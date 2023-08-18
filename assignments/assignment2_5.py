
# Program to check if a number is prime or not

def chkprime(no):
    flag = False

    if no == 1:
        print(num, "is not a prime number")
    elif no > 1:
        for i in range(2, no):
            if (no % i) == 0:
                flag = True
                break

    if flag:
        print(no, "is not a prime number")
    else:
        print(no, "is a prime number")        


def main():
    print("Enter a no")
    num=int(input())

    chkprime(num)







    
    

if __name__=="__main__":
    main()