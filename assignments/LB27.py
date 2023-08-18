#Enter value
#10
#2	4	6	8	10	12	14	16	18	20	

def evendi(no):
    for i in range(1,no*2):
        if(i%2)==0:
            print(i,end=" ")
            




def main():
    print("Enter a value ")
    num=int(input())

    evendi(num)

if __name__=="__main__":
    main()