#  Используя цикл while, найдите первое целое число, которое не кэшируется в памяти
a = 0
b = 0

while id(a) == id(b):
    a += 1
    b += 1
    print(id(a))
    print(id(b))
print(a)