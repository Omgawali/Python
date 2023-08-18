
def pattern(no):
    for i in range(no,0,-1):
        for j in range(i):
            print("*",end=" ")
        print("")    


def main():
    print("Enter a no")
    num=int(input())

    pattern(num)

if __name__=="__main__":
    main()