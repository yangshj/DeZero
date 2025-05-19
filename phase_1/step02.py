import numpy as np

from phase_1.step01 import Variable


class Function:
    def __call__(self, input):
        x = input.data
        y = self.fowrard(x)
        output = Variable(y)
        return output

    def fowrard(self, x):
        raise NotImplementedError


class Square(Function): # 入参是类则表明继承某个类
    def fowrard(self, x):
        return x ** 2

x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(x))
print(y.data)