#accept two string from user and copy the content of second string in last of first
def contntcopy(chr,chrr):
    
    chr+=chrr
    return chr     

def main():
    print("Enter a string")
    chhj=input()
    print("Enter another string")
    chj=input()
    re=contntcopy(chhj,chj)
    print(re)

if __name__=="__main__":
    main()