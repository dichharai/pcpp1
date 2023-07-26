import copy

class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = [price]
        self.weight = weight

    def __str__(self):
        return f"{self.name}, price: {self.price}, weight: {self.weight}"

d1 = Delicacy("Gelatos", [3.23], 1)
print(d1)
# shallow copy
d1_c = copy.copy(d1)

d1.price.append(5.23)
print(d1_c)
print(d1)

# deep copy
d2 = Delicacy("Mochi", [4.3], 4)
d2_dc = copy.deepcopy(d2)

d2.price.append(5.23)
print(d2_dc)
print(d2)
