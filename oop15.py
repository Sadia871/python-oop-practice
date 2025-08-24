class A:
    def method_a(self):
        print( "Method A from class B")
class B(A):
    def method_b(self):
        print("Method B from class C")
class C(B):
    def method_c(self):
        print("Method C from class A")
c = C()
c.method_a()
c.method_b()
c.method_c()
# Output:
# Method A from class A
# Method B from class B
# Method C from class C
# In this example, class C inherits from class B, which in turn inherits from class A. This creates a multilevel inheritance hierarchy where class C has access to methods from both class B and class A.
#         

