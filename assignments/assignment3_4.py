

def addlist(arrl,numb):
    icnt=0
    for i in range(len(arrl)):
        if(arrl[i]==numb):
            icnt=icnt+1

    return icnt           


def main():
    print("Enter number of elements :")
    length=int(input())
    
    arr=list()
    print("Enter element ")
    for i in range(length):
        value=int(input())
        arr.append(value)

        
     
    print("Enter element to search")
    num=int(input()) 
    result= addlist(arr,num)
    print("output",result)


if __name__=="__main__":
    main()