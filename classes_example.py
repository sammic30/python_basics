class myClass():
    def method1(self):
        print("my class method1")

    def method2(self, sstring):
        print("my class method 2" + sstring)

class anotherClass(myClass):
    def m1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def m2(self, sstring):
        print("anotherClass method2")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a String")

    c2 = anotherClass()
    c2.m1()
    c2.m2(" " + "This is another string")

if __name__ == "__main__":
    main()