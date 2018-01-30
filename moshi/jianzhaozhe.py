class Burger:
    name = ""
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
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0

class Snack():
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0
#建造者模式
class order:
    burger = ''
    snack = ''
    beverage = ''
    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage
    def show(self):
        print('Burger:%s' % self.burger.getName())
        print('Snack:%s' % self.snack.getName())
        print('Beverage:%s' % self.beverage.getName())

class orderBuilder:
    bBurger = ''
    bSnack = ''
    bBeverage = ''
    def addBurger(self, xBurger):
        self.bBurger = xBurger
    def addSnack(self, xSnack):
        self.bSnack = xSnack
    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage
    def build(self):
        return order(self)

if __name__ == '__main__':
    order_build = orderBuilder()
    order_build.addBurger(spicyChickenBurger())
    order_build.addSnack(chips())
    order_build.addBeverage(milk())
    order_1 = order_build.build()
    order_1.show()

"""
优点：
1、封装性好，用户可以不知道对象的内部构造和细节，就可以直接建造对象；
2、系统扩展容易；
3、建造者模式易于使用，非常灵活。在构造性的场景中很容易实现“流水线”；
4、便于控制细节。
使用场景：
1、目标对象由组件构成的场景中，很适合建造者模式。例如，在一款赛车游戏中，车辆生成时，需要根据级别、环境等，
选择轮胎、悬挂、骨架等部件，构造一辆“赛车”；
2、在具体的场景中，对象内部接口需要根据不同的参数而调用顺序有所不同时，可以使用建造者模式。例如：一个植物养殖器系统，对于某些不同的植物，
浇水、施加肥料的顺序要求可能会不同，因而可以在Director中维护一个类似于队列的结构，在实例化时作为参数代入到具体建造者中。
"""
