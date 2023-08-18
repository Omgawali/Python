
#Accept one the number for user and print that number of * on screen

def func(no):
    for i in range(no):
        print("*")

def main():
    print("Enter a number")
    num=int(input())
    func(num)

if __name__=="__main__":
    main()
