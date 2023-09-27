#Maximum and minimum of an array using minimum number of comparisons
def find_min_max(arr):
    if not arr:
        return None, None

    min_val = max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val

def main():

    
    #arr = [34, 56, 75, 234, 54]
    arr=[]
    num=int(input("Enter size of list"))
    for i in range(num):
        arr.append(int(input()))

    min_val, max_val = find_min_max(arr)
    print("Minimum:", min_val)
    print("Maximum:", max_val)

if __name__=="__main__":
    main()