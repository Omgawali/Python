def sub(A,B):
    return A-B

def SmartSub(fptr1):
    def Inner(a,b):
        if a<b:
            a,b=b,a
        return fptr1(a,b)
    return Inner        

def main():
    subx=SmartSub(sub)
    ret=subx(10,7)
    print(ret)

    ret=subx(7,10)
    print(ret)


if __name__=="__main__":
    main()