# Задача: 2. Намерете времето с най-големи продажби
# Вие сте собственик на online магазин, и искате да проверите в кои дни и часове има най-много продажби.
# Най-много продажби означава сумата на тези продажби, не броят на извършените продажби.
# Свалете файла sales.csv, който съдържа 1000 продажби. Файлът е CSV като първата колона е датата и часа на
# продажбата, втората колона е сумата на продажбата. Файлът не е подреден.
# Напишете код, който показва в кой ден е имало най-много продажби като сума от всички продажби за този ден.
# Пример: В понеделник е имало продажби за 2000 лева, във вторник за 2345 лева, а в сряда за 897 лева. Денят с най-много
# продажби е вторник. Разширение на задачата
# Разширете кода си, така че да показва в кой час има най-много продажби. Интересува ни часа, а не деня.
# Пример: За целия период между 13:00 и 14:00 е имало продажби за 897 лева, между 14:00 и 15:00 е имало продажби за 456 лева.
# Между 13:00 и 14:00 е имало повече продажби отколкото между 14:00 и 15:00

from datetime import datetime, date, timedelta
FNAME = 'C:/Users/lranchev.BOS-WPTSD/Desktop/sales.csv' #file to work with


def total_sales(FNAME):
    total = float()
    with open(FNAME,"r",encoding="utf-8") as sales:
        for record in sales:
            record = record.split(",")
            total += float(record[1])
    return total
#
# totals = total_sales(FNAME)
# print ("Total sales: ${}".format(round(totals,2)))


def total_sales_per_hour(FNAME):
    total = float()
    hour = set()
    list_of_hours = ()
    with open(FNAME,"r",encoding="utf-8") as sales:
        for record in sales:
            #record = record.split(",")
            hour.add(record[11:13])
    #list_of_hours = (hour)
    return hour




hours = total_sales_per_hour(FNAME)
# print ("Sales between the hours of {} and {}". format(hours, hours+1))
max_amount_final = []
best_hour = int()
for i in hours:
    total_per_hour = float()
    max_amount = []

    with open(FNAME,"r",encoding="utf-8") as sales:
        for record in sales:
            recordx = record.split(",")
            if i == record[11:13]:
                total_per_hour += float(recordx[1])

    if len(max_amount_final):
        if total_per_hour >= max_amount_final[0]:
            max_amount_final.pop()
            max_amount_final.append(total_per_hour)
            best_hour = i
    else:
        max_amount_final.append(total_per_hour)
        best_hour = i
best_hour_range = int(best_hour) + int(1)
#print (best_hour_range)
print ("Sales between hours of {} o'clock to {} o'clock are the best with total amount of ${}!!".format(best_hour, best_hour_range,  round(max_amount_final[0],2)) )

