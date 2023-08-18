#Accept number from user and check and check whether number is even or odd 


def func(no):
    if(no%2==0):
        print("even")
    else:
        print("odd")    


def main():
    print("Enter a number")
    num=int(input())
    func(num)

if __name__=="__main__":
    main()
