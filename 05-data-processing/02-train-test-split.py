import random

def train_test_split(data, test_ratio, seed= None):
    if not 0 < test_ratio <1:
        raise ValueError("test_ratio must be greater than 0 and smaller than 1")

    if len(data) <2:
        raise ValueError("data must contain at least 2 items")

    #copy 
    shuffled_data = data.copy()

    random_generator = random.Random(seed)
    random_generator.shuffle(shuffled_data)

    test_size = int(len(shuffled_data) * test_ratio)

    if test_size == 0:
        test_size = 1

    train_data = shuffled_data[:-test_size]
    test_data = shuffled_data[-test_size:]

    return train_data, test_data

data = [1,2,3,4,5,6,7,8,9,10]

train,test = train_test_split(data, 0.2, seed = 42)

print("Original:", data)
print("Train: ", train)
print("Test: ", test)
