class A:
    def method(self):
        print("Method from class A")
    pass

class B(A):
    def method(self): # This method overrides the method from class A
        print("Method from class B")
    pass

class C(A):
    def method(self):  # This method overrides the method from class A
        print("Method from class C")
    pass

class D(B, C):
    pass


d = D()
d.method()