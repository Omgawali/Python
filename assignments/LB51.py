#Input:
#N = 6
#arr[] = 7 10 4 3 20 15
#K = 3
#Output : 7
#Explanation :
#3rd smallest element in the given 
#array is 7.

def smallestno(arr,num1):
    print(arr)
    print(num1)

def main():
    arr=[]
    num=int(input("Enter size of list"))
    for i in range(num):
        arr.append(int(input()))
    num1=int(input("Enter a element"))

    smallestno(arr,num1)    

if __name__=="__main__":
    main()