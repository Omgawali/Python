
#Enter value
#4
#Enter values
#4
#A       B       C       D
#b       b       b       b
#c       c       c       c
#d       d       d       d   14.2

def abc(no1,no2):
    chj='a'
    ch='A'

    for i in range(1,no1+1):
        
        
        for j in range(1,no2+1):
            
            
            if i==1:    
                print(ch,end='\t')
            else:
                print(chj,end='\t')  
            ch= chr(ord(ch) +1)
        chj= chr(ord(chj) +1)          
        print() 
        


def main():
    print("Enter a no")
    num1=int(input())
    print("Enter another no")
    num2=int(input())

    abc(num1,num2)


if __name__=="__main__":
    main()