#accept string from user and reverse string in place  
def chrpresent(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

    #op=chj[::-1]
    #return op


def main():
    print("Enter a string")
    inp=input()
    
    re=chrpresent(inp)
    print(re)

if __name__=="__main__":
    main()