# Лекция: 5. Голяма задача Курс: Python 3  # Задача: 1. Анализ на данни от верига магазини
# Разполагаме с каталог на стоки и данни за продажби на голям производител на спортни стоки,
# и трябва да направим анализ на тази информация.
# Обобщение
# ---------
#     Общ брой продажби: 10000
#     Общо сума продажби: 3191507.82 €
#     Средна цена на продажба: 319.15 €
#     Начало на период на данните: 2015-12-01T08:00:48+01:00
#     Край на период на данните: 2016-01-24T20:49:38+00:00

# import os
# import sys
# from datetime import datetime, date, timedelta

# files to work with
FNAME_SALES = 'C:/Users/lranchev.BOS-WPTSD/Desktop/sales-10K.csv'
# FNAME_SALES = 'C:/Users/lranchev.BOS-WPTSD/Desktop/sales-1M.csv'
FNAME_CATALOG = 'C:/Users/lranchev.BOS-WPTSD/Desktop/catalog.csv'
COUNT = 0


# total amount of sales
def total_amount_sales(FNAME):
    total = float()
    count = 0
    with open(FNAME, "r", encoding="utf-8") as sales:
        for record in sales:
            record = record.split(",")
            total += float(record[-1])
    return total


# total  sales
def total_sales(FNAME):
    count = 0
    with open(FNAME, "r", encoding="utf-8") as sales:
        for record in sales:
            count += 1
    return count


# find 1st and last sale's date
def first_last_date(FNAME):
    uniq_dates = []
    uniq = str()
    first_date = str()
    last_date = str()
    with open(FNAME, "r", encoding="utf-8") as sales:
        for record in sales:
            record = record.split(",")
            uniq_dates.append(record[3])
            first_date = uniq_dates[0]
            last_date = uniq_dates[-1]
    return (first_date, last_date)


# Amount of sales per category

def sale_per_category(FNAME: object, FNAME_SALES: object) -> object:
    uniq_category = {}
    with open(FNAME, "r", encoding="utf-8") as sales:
        for record in sales:
            record = record.split(",")
            uniq_category.update({record[0]: record[5]})
    final_dic = {}
    for key, values in uniq_category.items():
        with open(FNAME_SALES, "r", encoding="utf-8") as sales:
            for record in sales:
                # print (values)
                record = record.split(",")
                amount = float(record[-1])
                id = record[0]
                if values not in final_dic and key == id:
                    final_dic[values] = [amount]
                elif values in final_dic and key == id:
                    final_dic[values].append(amount)
                else:
                    # print("Error occurred. Please check your code, Dude!")
                    # break
                    None
    return final_dic


# Amount of sales per cities

def sale_per_cities(FNAME_SALES: object) -> object:
    uniq_cities = set()
    with open(FNAME_SALES, "r", encoding="utf-8") as sales:
        for record in sales:
            record = record.split(",")
            uniq_cities.add(record[2])
    final_dic_cities = {}
    for uniq_city in uniq_cities:
        with open(FNAME_SALES, "r", encoding="utf-8") as sales:
            for record in sales:
                # print (values)
                record = record.split(",")
                amount = float(record[-1])
                id = record[2]
                if uniq_city not in final_dic_cities and uniq_city == id:
                    final_dic_cities[uniq_city] = [amount]
                elif uniq_city in final_dic_cities and uniq_city == id:
                    final_dic_cities[uniq_city].append(amount)
                else:
                    # print("Error occurred. Please check your code, Dude!")
                    # break
                    None
    return final_dic_cities


# Amount of sales per hour


def sale_per_hour(FNAME_SALES: object) -> object:
    uniq_hours = set()
    with open(FNAME_SALES, "r", encoding="utf-8") as sales:
        for record in sales:
            record = record.split(",")
            uniq_hours.add(record[3])
    final_dic_hours = {}
    for uniq_hour in uniq_hours:
        with open(FNAME_SALES, "r", encoding="utf-8") as sales:
            for record in sales:
                # print (values)
                record = record.split(",")
                amount = float(record[-1])
                id = record[3]
                if uniq_hour not in final_dic_hours and uniq_hour == id:
                    final_dic_hours[uniq_hour] = [amount]
                elif uniq_hour in final_dic_hours and uniq_hour == id:
                    final_dic_hours[uniq_hour].append(amount)
                else:
                    # print("Error occurred. Please check your code, Dude!")
                    # break
                    None
    return final_dic_hours


# ***PRINTING ON SCREEN****
# *************************
# *************************
print("Summary")
print("-" * 10)
total_sales = total_sales(FNAME_SALES)
total_amount_sales = total_amount_sales(FNAME_SALES)
first_last_date = first_last_date(FNAME_SALES)

print("    Total sales: {}".format(total_sales))
print("    Total amount of sales: ${}".format(round(total_amount_sales, 2)))
print("    Average of sales: ${}".format(round(total_amount_sales / total_sales, 2)))
print("    First sale was completed on: {}".format(first_last_date[0]))
print("    Last sale was completed on: {}".format(first_last_date[1]))

print("\nAmount of sales per category (top 5)")
print("-" * 10)
sale_per_category = dict(sale_per_category(FNAME_CATALOG, FNAME_SALES))

categorytop5 = []
amounttop5 = []
amounttop5_loop = []
for key, values in sale_per_category.items():
    total_value = sum(values)
    amounttop5_loop = amounttop5
    if len(categorytop5) == 0:
        categorytop5.append(key)
        amounttop5.append(total_value)
    else:
        for idx, max_valuu in enumerate(amounttop5_loop):
            if max_valuu < total_value and total_value not in amounttop5:
                categorytop5.insert(idx, key)
                amounttop5.insert(idx, total_value)
            elif total_value not in amounttop5 and len(categorytop5) == 1:
                categorytop5.append(key)
                amounttop5.append(total_value)
            else:
                None

for i in range(5):
    print("    {} : ${}".format(str(categorytop5[i]).replace("\"", ""), round(amounttop5[i], 2)))

print("\nAmount of sales per cities (top 5)")
print("-" * 10)

sale_per_cities = dict(sale_per_cities(FNAME_SALES))
# print(sale_per_cities)
citytop5 = []
amounttop5 = []
amounttop5_loop = []
for key, values in sale_per_cities.items():
    total_value = sum(values)
    amounttop5_loop = amounttop5
    if len(citytop5) == 0:
        citytop5.append(key)
        amounttop5.append(total_value)
    else:
        for idx, max_valuu in enumerate(amounttop5_loop):
            if max_valuu < total_value and total_value not in amounttop5:
                citytop5.insert(idx, key)
                amounttop5.insert(idx, total_value)
            elif total_value not in amounttop5 and len(citytop5) == 1:
                citytop5.append(key)
                amounttop5.append(total_value)
            else:
                None
# print (citytop5)
for i in range(5):
    print("    {} : ${}".format(str(citytop5[i]).replace("\"", ""), round(amounttop5[i], 2)))

print("\nAmount of sales per hour (top 5)")
print("-" * 10)

sale_per_hour = dict(sale_per_hour(FNAME_SALES))
# print(sale_per_cities)
hourtop5 = []
amounttop5 = []
amounttop5_loop = []
for key, values in sale_per_hour.items():
    total_value = sum(values)
    amounttop5_loop = amounttop5
    if len(hourtop5) == 0:
        hourtop5.append(key)
        amounttop5.append(total_value)
    else:
        for idx, max_valuu in enumerate(amounttop5_loop):
            if max_valuu < total_value and total_value not in amounttop5:
                hourtop5.insert(idx, key)
                amounttop5.insert(idx, total_value)
            elif total_value not in amounttop5 and len(hourtop5) == 1:
                hourtop5.append(key)
                amounttop5.append(total_value)
            else:
                None
# print (hourtop5)
for i in range(5):
    print("    {} : ${}".format(str(hourtop5[i]).replace("\"", ""), round(amounttop5[i], 2)))



#
# if len(sys.argv) == 3:
#     whattosearch = sys.argv[2]
#     wheretosearch = sys.argv[1]
#     filesfound = find_the_file(whattosearch, wheretosearch)
#     if len(filesfound):
#         for each_file in filesfound:
#             print ( "This file was located -->", each_file)
#     else:
#         print (None , "was found. Please try again!")
# else:
#     print("Please make sure to supply where and what to search for")
