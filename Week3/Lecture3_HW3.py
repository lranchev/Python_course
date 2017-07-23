# Задача: 3. Променете цените в каталог  Назад Идва "Черният петък", и Вие сте собственик на магазин за спортни стоки в Бургас.
# Две седмици преди голямото пазаруване решавате да увеличите цените на всички артикули със 75%, за да може по време на "Черния петък"
# да обявите "отстъпки" от 50%. За целта трябва да напишете програма, която прочита каталога от CSV файл, увеличава
# всяка една цена със 75% и записва резултата в друг CSV файл. Структурата на файла, който ще запишете, и данните в него трябва да са
# единтични, с изключение на цените, разбира се.Ако желаете, може да разширите логиката, като увеличите с различен процент разлините
# категории стоки (обувки, чанти, якета...).
#
def file_len(fname):
    with open(fname, 'r', encoding='utf-8') as fileread:
        for i, l in enumerate(fileread):
            pass
    return i + 1

FNAME = 'C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_sample.csv'
FNAME1 = 'C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_full.csv'
FTARGET = 'C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_sample_75up.csv'
FTARGET1 = 'C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_full_75up.csv'
FILELEN = (file_len(FNAME))
FILELEN1 =  (file_len(FNAME1))
COUNT = 0
with open(FNAME, 'r', encoding='utf-8') as fileread:
    with open (FTARGET, 'w', encoding= 'utf-8') as filewrite:


        for line in fileread:
            val = line.split(",")
            amount = round(float ((line.split(",")[6]).rstrip("\n")),2)
            new_amount = str(round(amount * 1.75,2))
            val.pop()
            val.append(new_amount)
            new_line = str()
            for z in val:
                if len(new_line):
                    new_line += ","
                    new_line += z
                else:
                    new_line = z
            COUNT += 1
            if COUNT == FILELEN:
                filewrite.write(new_line)
            else:
                filewrite.write(new_line + "\n")
print ("Lines converted -", COUNT)
