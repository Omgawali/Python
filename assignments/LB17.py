#check a no whether it contains 0 in it or not

def zero(no):
    while(no!=0):
        iSum=no%10 
        if(iSum==0):
            return True            
        no=no/10

    return False



def main():
    print("Enter a no :")
    num=int(input())

    ians=zero(num)
    if(ians==True):
        print("O is there in it")
    else:
        print("Not in it")    



if __name__=="__main__":
    main()