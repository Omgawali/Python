

# *	 #	#
# *  *	#
# *  *	* 
def pattrn(no1,no2):
    if(no1!=no2):
        print("Invalid put")
    for i in range(no1):
        print(" ")
        for j in range(no2):
            if(i>j):
                print("*",end="\t")
            elif(i<j):
                print("#")        
 


def main():
    num=int(input("Enter a no"))
    num1=int(input("Enter another no"))

    pattrn(num,num1)


if __name__=="__main__":
    main()