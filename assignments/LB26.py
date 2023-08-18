#Enter value
#5
#	1	*	#	2	*	#	3	*	#	4	*	#	5	*

def pptr(no):
    for i in range(no):
        print(i," *  # ",end=" ")

def main():
    print("Enter a no ")
    num=int(input())

    pptr(num)

if __name__=="__main__":
    main()