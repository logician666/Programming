class Delicacy:
    def __init__(self, name, price, weight):
        self.name, self.price, self.weight = name, price, weight
    
    def __str__(self):
        return f"{self.name} candy weighting {self.weight} units and costing {self.price} per unit."

warehouse = list()
warehouse.append(Delicacy(name='Lolly Pop', price=0.4, weight=133))
warehouse.append(Delicacy(name='Licorice', price=0.1, weight=251))
warehouse.append(Delicacy(name='Chocolate', price=1, weight=601))
warehouse.append(Delicacy(name='Sours', price=0.01, weight=513))
warehouse.append(Delicacy(name='Hard candies', price=0.3, weight=433))

import copy

new_warehouse = copy.deepcopy(warehouse)
for item in new_warehouse:
    if item.weight > 300:
        item.price *= 0.8

print('*'*20)
print('Source list of candies')
for item in warehouse:
    print(item)

print('*'*20)
print('Price proposal')
for item in new_warehouse:
    print(item)
