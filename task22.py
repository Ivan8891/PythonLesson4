n = int(input("Введите колличество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
list_1 = []
list_2 = []
listSort = []
for i in range(n):
	list_1.append(int(input("Введите число для первого множества: ")))
print(f"Ваше первое множество: {list_1}")
for i in range(m):
	list_2.append(int(input("Введите число для второго множества: ")))
print(f"Ваше второе множество: {list_2}")
set = set(list_1).union(set(list_2))
listSort = list(set)
list.sort(listSort)
print(f"Результат слияния множеств: {listSort}")
