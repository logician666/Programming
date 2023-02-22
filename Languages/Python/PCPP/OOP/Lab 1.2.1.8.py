import random

class Apple:
    count, total_weight = 0, 0
    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        Apple.total_weight += self.weight
        Apple.count += 1

apples = []
while Apple.count < 1000 and Apple.total_weight < 300:
    apples.append(Apple())

print(f'{Apple.count} apples has been collected at a total weight of {Apple.total_weight:.2f} units.')