#  Отфильтровать из заданного списка только четные элементы.[-2, -1, 0, 1, -3, 2, -3]

def positive(x):
    return x % 2 == 0


L = [-2, -1, 0, 1, -3, 2, -3]
result = filter(positive, L)
print(list(result))