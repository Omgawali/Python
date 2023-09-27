#accept string and count no of white spaces

def count_spaces(chj):
    cnt = 0
    for char in chj:
        if char == ' ':
            cnt += 1
    return cnt

def main():
    chr = input("Enter a string: ")
    re = count_spaces(chr)
    print("Number of white spaces:", re)
if __name__ == "__main__":
    main()