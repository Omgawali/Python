 

def pattrn(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
 
def main():
    print("Enter a no")
    num=int(input())

    pattrn(num)

if __name__=="__main__":
    main()    