#accept string from and count no of capital charachter 

def alpha(b):    
    return (b >='A')and(b<='Z')


def main():

    a=0
    print("Enter a character")
    ch=str(input())
    op1=list(filter(alpha,ch))
    for i in op1:
        a+=1
    print("Captial characters are",a)    

if __name__=="__main__":
    main()