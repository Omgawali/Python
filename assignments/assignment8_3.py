
i=5
def recur(no):
    global i
    if(i>no):
        print(i)
        i-=1
        recur(no)

def main():
    recur(0)

if __name__=="__main__":
    main()