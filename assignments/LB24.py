
#ip   n    6
#          8225   665   3   76   953    858 
#         8+2+2+5  
#          17      17    3   13   17      21

def addofd(no):
    
    for i in range(len(no)):
        isum=0
        while(no[i]!=0):
            idigfiti=no[i]%10
            
            isum=isum+idigfiti
            no[i]=no[i]//10
        print(isum)
    


    

def main():
    print("Enter number of elements :")
    length=int(input())
    
    arr=list()
    print("Enter element ")
    for i in range(length):
        value=int(input())
        arr.append(value)

#    print("Elements from list are :")
#    for i in range(len(arr)):
#        print(arr[i])

    addofd(arr)    


if __name__=="__main__":
    main()
