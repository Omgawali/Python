
class Demo:
    value=10
    def __init__(self,num1,num2):  # Constructor
        self.no1 = num1   # Instance Variable
        self.no2 = num2       # Instance Variable

    def Fun(self):
        print("First number is",self.no1)

    def Gun(self):
        print("Second number is",self.no2)


def main():
    obhj1=Demo(11,201)
    obhj2=Demo(51,101)

    obhj1.Fun()
    obhj2.Gun()
    obhj2.Fun()
    obhj1.Fun()

if __name__=="__main__":
    main()