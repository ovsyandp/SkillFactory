# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
def func(*nums):
    p = 1
    for i in nums:
        p = p*i
    return p


print(int(func(4, 10, 10, 2.5)))