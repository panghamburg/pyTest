class Burger():
    name = ''
    price = 0.0
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0
#食物工厂
class foodFactory():
    type = ''
    def createFood(self, foodClass):
        print(self.type, "factory produce a instance.")
        foodIns = foodClass()
        return foodIns
#简单工厂
class simpleFoodFactory():
    @classmethod
    def createFood(cls, foodClass):
        print("Simple factory produce a instance.")
        foodIns = foodClass()
        return foodIns
#具体的工厂
class burgerFacroty(foodFactory):
    def __init__(self):
        self.type = 'BURGER'
class snackFactory(foodFactory):
    def __init__(self):
        self.type = 'SNACK'
class beverageFactory(foodFactory):
    def __init__(self):
        self.type = 'BEVERAGE'

#使用工厂
if __name__ == '__main__':
    burger_factory = burgerFacroty()
    burger_factory_simple = simpleFoodFactory()
    cheese_burger = burger_factory.createFood(cheeseBurger)
    print(cheese_burger.getName(), cheese_burger.getPrice())
    cheese_burger_simple = burger_factory_simple.createFood(cheeseBurger)
    print(cheese_burger_simple.getName(), cheese_burger_simple.getPrice())

"""
工厂模式、抽象工厂模式的优点：
1、工厂模式巨有非常好的封装性，代码结构清晰；在抽象工厂模式中，其结构还可以随着需要进行更深或者更浅的抽象层级调整，非常灵活；
2、屏蔽产品类，使产品的被使用业务场景和产品的功能细节可以分而开发进行，是比较典型的解耦框架。
工厂模式、抽象工厂模式的使用场景：
3、当系统实例要求比较灵活和可扩展时，可以考虑工厂模式或者抽象工厂模式实现。比如，
在通信系统中，高层通信协议会很多样化，同时，上层协议依赖于下层协议，那么就可以对应建立对应层级的抽象工厂，根据不同的“产品需求”去生产定制的实例。

不足
1、工厂模式相对于直接生成实例过程要复杂一些，所以，在小项目中，可以不使用工厂模式；
2、抽象工厂模式中，产品类的扩展比较麻烦。毕竟，每一个工厂对应每一类产品，产品扩展，就意味着相应的抽象工厂也要扩展。
"""
