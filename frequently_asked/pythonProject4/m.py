class Myclass:
    def f(self):
        print("f")
def m_f():
    print("monkey patched")

Myclass.f = m_f
obj=Myclass()
obj.f()

