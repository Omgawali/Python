#chk whether it is digit or not


def main():

    a=0
    print("Enter Digits")
    ch=str(input())
    #checking all elements to be numeric using isdigit()
    res = list(filter(lambda x: x.isdigit(), ch))
 
    if(len(res) == len(ch)):
        print("True")
    else:
        print("False")


if __name__=="__main__":
    main()