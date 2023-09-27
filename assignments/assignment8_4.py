
digit=0
sum=0

def recur(no):
    
    global idigit
    global sum

    if(no>0):
        idigit=no%10
        sum=sum+idigit
        no=no//10
        recur(no)

    return sum    
    

def main():
    num=recur(879)
    print(num)

if __name__=="__main__":
    main()