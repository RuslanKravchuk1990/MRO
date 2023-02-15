# MRO exemple.
class A:
    VAR = 'A'
    VAR2 = 'A2'
    def method(self):
        print(self.VAR + self.VAR2)

class B(A):
    VAR = 'B'
    def method(self):
        print(self.VAR + self.VAR2)

class C(B, A):
    pass

class D(C):
    pass

print(D.__mro__)
print(D.mro())

