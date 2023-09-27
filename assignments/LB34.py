#Enter value:
#4
#Enter values:
#5
#1	2	3	4	5	
#6	7	8	9	10	
#11	12	13	14	15	
#16	17	18	19	20	


def abcd(no1,no2):
    a=0
    for i in range(no1):
        for j in range(no2):
            a=a+1
            print(a,end='\t')
        print()
            

def main():
    num=int(input("Enter a no"))
    num1=int(input("Enter another no"))

    abcd(num,num1)


if __name__=="__main__":
    main()