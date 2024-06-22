# Напишите цикл, который ищет наибольший элемент в матрице.
max_number = 0
test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]
for i in test_matrix:
    for b in i:
        if b > max_number:
            max_number = b
print(max_number)
