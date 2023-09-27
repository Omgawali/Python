#character occur at and how many time

def chrpresent(chj,chr1):
    icnt1=0
    icnt=0
    for char in chj:
        icnt1+=1
        if char==chr1:
            icnt+=1
            print("character occur at",icnt1,"position")
            
    return icnt

def main():
    print("Enter a string")
    inp=input()
    inp1=input("Enter a character")
    re=chrpresent(inp,inp1)
    print(re)

if __name__=="__main__":
    main()