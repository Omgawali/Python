#accept one number and print that no of even no on screen

def func(no):
    for i in range(no):
        if(i%2==0):
            print(i)

def main():
    print("Enter a no ")
    num=int(input())
    func(num)

if __name__=="__main__":
    main()