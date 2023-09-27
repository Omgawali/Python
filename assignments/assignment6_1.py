
class BookStore:
    NoOfBooks=0
    def __init__(self,namee,authorr):
        self.name=namee
        self.author=authorr
        BookStore.NoOfBooks=BookStore.NoOfBooks+1
    
    def Display(self):
        print("books is",self.name)
        print("authot is",self.author)
        print("no of books",self.NoOfBooks)

def main():
    obhj1=BookStore('Linux system programming','RobertLove')
    obhj1.Display()
    obhj2=BookStore('C programming','Dennis ricchie')
    obhj2.Display()
    print()

if __name__=="__main__":
    main()