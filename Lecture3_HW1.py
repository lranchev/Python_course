"""
Задача: 1. Намерете средната цена на продукт от текстов файл Назад
Свалете тези два файла (catalog_sample.csv) и (catalog_full.csv) Файловете са реален продуктов каталог на на известен производител на спортни
стоки, с описание и цени (цените са произволни), като разликата между двата файла е в броя на артикулите. catalog_sample има само 200
артикула, докато catalog_full има над 60000. Структурата на двата файла е еднаква.
catalog_sample.csv catalog_full.csv
Напишете програма, която намира средната цена от всички артикули във файла. Структурата на CSV файловете е следната: каталожен номер
име на продукта цветове на продукта. Ако са повече от един са разделени с / за какъв вид активност е предназначен артикула каква е групата на артикула
за кой пол и възраст е предназначен артикула цена Разделителят на данните е , (запетая), а десетичният знак е . (точка)
"""
total = []
with open('C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_sample.csv') as f:
    for idx, line in enumerate(f):
        #print(line.split(",")[6],end="")
        #print("*"*6)
        h = float ((line.split(",")[6]).rstrip("\n"))
        total.append(h)
    print(round(sum(total)/len(total),2))


with open('C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_full.csv') as f2:
    for line in f2:
        total.append(float ((line.split(",")[6]).rstrip("\n")))
    print (round(sum(total)/len(total),2))
