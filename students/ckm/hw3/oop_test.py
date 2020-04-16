"""class Parent(object):
    def implicit(self):
        print("PARENT IMPLICIT()")
    def override(self):
        print("PARENT override()")
    def altered(self):
        print("PARENT altered()")
    
class Child(Parent):
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("Child,before Parent")
        super(Child,self).altered()
        print("CHILD,AFTER PARENT ALTERED()")
dad = Parent()
son = Child()        
dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()"""
class Other(object):
    def override(self):
        print("Other override()")
    def implicit(self):
        print("Other implicit()")
    def altered(self):
        print("OTHER altered")
        self.other.altered()
        print("CHILD,AFTER OTHER ALTERED()")
son=Child()
son.implicit()
son.override()
son.altered()
