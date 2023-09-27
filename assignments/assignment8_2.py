
i=1
def recur(no):
    global i
    if(i<=no):
        print(i)
        i+=1
        recur(no)

def main():
    recur(5)

if __name__=="__main__":
    main()