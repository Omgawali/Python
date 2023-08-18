#accept one no from user and print even factor of that no
#input 36
#op 2 6 12 18

def func(no):
    for i in range(1,no):
        if ((i%2==0) and (no%i==0)):
            print(i)

def main():
    print("Enter a no ")
    num=int(input())
    func(num)

if __name__=="__main__":
    main()