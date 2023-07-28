listBerry = []
bush = int(input("Введите количество кустов: "))
for i in range(bush):
    listBerry.append(int(input("Ввелите количество ягод на кусте: ")))
print(listBerry)
sum = 0
res = 0
j = 0
while (j < bush):
    if (j == bush - 1):
        sum = listBerry[j - 1] + listBerry[j] + listBerry[0]
    else:
        sum = listBerry[j - 1] + listBerry[j] + listBerry[j + 1]
    if (sum > res):
        res = sum
        n = j + 1
    j += 1
print(f"Сбор с куста {n} принесет {res} ягод.")