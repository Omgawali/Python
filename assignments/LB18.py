#count frequency of 2


def zero(no):
    while(no!=0):
        iSum=no%10 
        if(iSum==2):
            return True            
        no=no//10

    return False



def main():
    print("Enter a no :")
    num=int(input())

    ians=zero(num)
    if(ians==True):
        print("2 is there in it")
    else:
        print("Not in it")    



if __name__=="__main__":
    main() 