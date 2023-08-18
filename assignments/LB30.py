#ip   5
#op   5 4 3 2 1

def reverse(no):
    for i in range(no,0,-1):
        print(i,end=" ")

def main():
    print("Enter a no ")
    num=int(input())

    reverse(num)

if __name__=="__main__":
    main()