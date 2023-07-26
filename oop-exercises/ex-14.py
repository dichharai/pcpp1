from datetime import datetime

def get_instantiation_time(self):
    return MyMeta.instantiation_time

class MyMeta(type):
    instantiation_time = ''
    classes = []

    def __new__(mcs, name, bases, dictionary):
        MyMeta.instantiation_time = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        if 'get_instantiation_time' not in dictionary:
            dictionary["get_instantiation_time"] = get_instantiation_time

        if name not in MyMeta.classes:
            MyMeta.classes.append(name)

        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class LunaMoth(metaclass=MyMeta):
    def __init__(self, color):
        self.color = color

class AtlasMoth(metaclass=MyMeta):
    def __init__(self, color):
        self.color = color

lm = LunaMoth("lime-green")
am = AtlasMoth("citrine")

print(f'Luna Moth creation at: {lm.get_instantiation_time()}')
print(f'Atlas Moth creation at: {am.get_instantiation_time()}')
print(f'classes created: {lm.__class__.classes}')

