#Enter value:
#4
#Enter values:
#4
#A	A	A	A	
#B	B	B	B	
#C	C	C	C	
#D	D	D	D	

def abcd(no1,no2):
    ch='A'
    for i in range(no1):
        for j in range(no2):
            print(ch,end='\t')
        print()
        ch=chr(ord(ch)+1)    

def main():
    num=int(input("Enter a no"))
    num1=int(input("Enter another no"))

    abcd(num,num1)


if __name__=="__main__":
    main()