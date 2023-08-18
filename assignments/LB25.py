#accept number from user and display below pattern


#ip   5
#op    5    #    4    #    3     #    2     #    1     #

def pptr(no):
    for i in range(no,0,-1):
        print(i,"#",end=" ")

def main():
    print("Enter a no ")
    num=int(input())

    pptr(num)

if __name__=="__main__":
    main()