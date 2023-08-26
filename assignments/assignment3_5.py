from functools import reduce

import MarvellousNum

def main():
    arr=[]
    print("Enter no of element")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        value=int(input())
        arr.append(value)

    result= list(map(MarvellousNum.checkPrime,arr))
    print(result)  

    result1=reduce(MarvellousNum.addlist,result)
    print(result1)  

        
if __name__=="__main__":
    main()        