#divide 2 no

def divideno(no1,no2):
    iAns=no1/no2
    print("Division of these no is",iAns)


def main():
    print("enter one no")
    num1=int(input())
    print("enter second no")
    num2=int(input())

    divideno(num1,num2)


if __name__== "__main__":
    main()