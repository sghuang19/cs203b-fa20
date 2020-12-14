class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()

str = 'abcdefghijklmnopqrstuvwxyz'
s = slice(5, 20, 2)
i = s.indices(10)
print(i)
print(str[1:3])
