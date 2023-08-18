#use to display non factor


def func(no):
   
    for i in range(no,0,-1):
        if ((no%i!=0)):
            print(i)
           

def main():
    print("Enter a no ")
    num=int(input())
    func(num)

if __name__=="__main__":
    main()
