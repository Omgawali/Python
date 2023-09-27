#Write a program to reverse an array or string
def reverse(chj):
    reversed_str=''
    for char in chj:
        reversed_str=char+reversed_str
    return reversed_str    

def main():
    print("Enter a string")
    chr=input()
    ch=reverse(chr)
    print(ch)

if __name__=="__main__":
    main()    