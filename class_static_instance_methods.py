class Example:
    count = 0  # class attribute

    def __init__(self, value):
        self.value = value  # instance attribute

    def instance_method(self):
        print(f'Instance value: {self.value}')

    @classmethod
    def class_method(cls):
        cls.count += 1
        print(f'Class count: {cls.count}')

    @staticmethod
    def static_method():
        print('Static method called')

exp = Example(1)
print(exp.count)
exp.instance_method()
exp.class_method()
exp.static_method()
print(exp.count)