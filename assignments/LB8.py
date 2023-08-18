#Accept two numbers from user and display first number is second number of times 


def func(no,no2):
    for i in range(no):
        print(no2)

def main():
    print("Enter a number")
    num=int(input())
    print("Enter another number")
    num2=int(input())
    func(num,num2)

if __name__=="__main__":
    main()
