import random
# # import my_module

# # random_integer = random.randint(1, 100)
# # print(random_integer)

# # print(my_module.my_favorite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)


random_head_or_tail = random.randint(0, 1)
if random_head_or_tail == 0:
    print("heads")
else:
    print("tails")
