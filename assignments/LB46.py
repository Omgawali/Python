#copy one string into anothjer

def chrpresent(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = reversed_str + char
    return reversed_str

def main():
    print("Enter a string")
    inp=input()
    
    re=chrpresent(inp)
    print(re)

if __name__=="__main__":
    main()