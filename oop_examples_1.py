class Base:
    def price(self):
        return 10
class InterFoo(Base):
    def price(self):
        return super().price() * 1.1
class Discount(InterFoo):
    def price(self):
        return super().price() * 0.8
#делаем сначала наценку 10%, потом скидку 20%
print(Discount().price())  #>>>>  8.8

