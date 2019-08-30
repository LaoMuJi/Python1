
class Z():

    def zzz(self):
        print("1")

    # 类方法
    @classmethod
    def abc(cls):
        print("2")

    # 静态方法
    @staticmethod
    def bcd():
        print("3")


z = Z()
z.zzz()
z.abc()
z.bcd()
