
def recur(n):
    
    if (n==1 or n==0):
        return 1 
    else:
        return (n*recur(n-1))

    

def main():
    num=recur(5)
    print(num)


if __name__=="__main__":
    main()