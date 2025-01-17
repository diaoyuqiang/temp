# class类继承中的super()方法

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        # super().bar(message)  # py3中可以省略括号里的内容
        
        print('Child bar fuction')
        # 继承父类的实例属性
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')