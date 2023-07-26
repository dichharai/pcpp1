import random

class ApplePackaging:
    apples_processed = 0
    WEIGHT_LIMIT = 300
    total_weight = 0

    def __init__(self, weight):
        self.weight = weight
        ApplePackaging.apples_processed += 1
        ApplePackaging.total_weight += self.weight
        

while(ApplePackaging.total_weight <= ApplePackaging.WEIGHT_LIMIT and ApplePackaging.apples_processed <= 1000):
    weight = random.uniform(0.2, 0.5)
    ApplePackaging(weight)

print(f'Number of apples processed: {ApplePackaging.apples_processed}')
print(f'Total weight of the apples processed: {round(ApplePackaging.total_weight, 1)}')