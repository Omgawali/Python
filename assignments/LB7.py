#Accept on number from user it number is less than 10 then print "Hello" otherwise print "Demo"

def func(no):
    if(no<10):
        print("Hello")
    else:
        print("Demo")    


def main():
    print("Enter a number")
    num=int(input())
    func(num)

if __name__=="__main__":
    main()
