#Enter value:
#4
#Enter values:
#5
#1	2	3	4	5	
#1	2	3	4	5	
#1	2	3	4	5	
#1	2	3	4	5	


def abcd(no1,no2):
    for i in range(1,no1):
        for j in range(1,no2):
            print(j,end='\t')
        print()
            

def main():
    num=int(input("Enter a no"))
    num1=int(input("Enter another no"))

    abcd(num,num1)


if __name__=="__main__":
    main()