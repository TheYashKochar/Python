import random
range_ = int(input('Enter Number of Q\'s : '))
num_list = random.sample(range(1, range_), 7)
print(sorted(num_list))