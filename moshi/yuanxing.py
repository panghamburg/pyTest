from copy import copy, deepcopy
#图层对象
class simpleLayer:
    background = [0, 0, 0, 0]
    content = 'blank'
    def getContent(self):
        return self.content
    def getBackgroud(self):
        return self.background
    def paint(self, painting):
        self.content = painting
    def setParent(self, p):
        self.background[3] = p
    def fillBackground(self, back):
        self.background = back
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)

if __name__ == "__main__":
    dog_layer = simpleLayer()
    dog_layer.paint('Dog')
    dog_layer.fillBackground([0, 0, 255, 0])
    print('Background:', dog_layer.getBackgroud())
    print('Painting:', dog_layer.getContent())
    another_dog_layer = dog_layer.deep_clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint('Puppy')
    print('Original Background:', dog_layer.getBackgroud())
    print('Original Painting:', dog_layer.getContent())
    print('Copy Background:', another_dog_layer.getBackgroud())
    print('Copy Painting:', another_dog_layer.getContent())


"""
优点：
1、性能极佳，直接拷贝比在内存里直接新建实例节省不少的资源；
2、简化对象创建，同时避免了构造函数的约束，不受构造函数的限制直接复制对象，是优点，也有隐患，这一点还是需要多留意一些。
使用场景：
1、对象在修改过后，需要复制多份的场景。如本例和其它一些涉及到复制、粘贴的场景；
2、需要优化资源的情况。如，需要在内存中创建非常多的实例，可以通过原型模式来减少资源消耗。此时，原型模式与工厂模式配合起来，不管在逻辑上还是结构上，都会达到不错的效果；
3、某些重复性的复杂工作不需要多次进行。如对于一个设备的访问权限，多个对象不用各申请一遍权限，由一个设备申请后，通过原型模式将权限交给可信赖的对象，既可以提升效率，又可以节约资源。
缺点
1、深拷贝和浅拷贝的使用需要事先考虑周到；
2、某些编程语言中，拷贝会影响到静态变量和静态函数的使用。
"""
