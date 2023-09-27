#accept charachter and check whether it is alphabet or not

def alpha(chj):
    if(chj >='A')and(chj<='Z')or(chj>='a')and(chj<='z'):
        return chj

def main():
    print("Enter a character")
    ch=str(input())
    op=alpha(ch)
    print(op)

if __name__=="__main__":
    main()