ls1 = [1, 2, 4, 0]
ls2 = [i ** 2 for i in ls1]
print(ls2)

frut1 = ['banana', 'apple', 'kiwi', 'watermelon']
frut2 = ['pineapple', 'melon', 'watermelon', 'apple']
frut3 = [f for f in frut1 if f in frut2]
print(frut3)


ls = [i for i in range(-10, 50) if i % 3 == 0 and i > 0 and i % 4 != 0]
print(ls)