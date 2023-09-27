#if character is present in it or not
def chrpresent(chj,chr1):
    flag=False
    for char in chj:
        if char==chr1:
            flag=True
            
    return flag        

def main():
    print("Enter a string")
    inp=input()
    inp1=input("Enter a character")
    re=chrpresent(inp,inp1)
    print(re)

if __name__=="__main__":
    main()