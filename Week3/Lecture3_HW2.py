# Задача: 2. Намерете средната цена на продукт от текстови файл, групирана по критерии Назад Използвайки кода си от предишната задача,
# и използвайки същите файлове, намерете средната цена от всички продукти в каталога, групирани по пол/възраст.
# Използвайте колоната №6 за пол и възраст.\
total = []
totalmen = []
totalwomen = []
totalkid = []
totalinfant = []
totalunisex = []
totalother = []
with open('C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_sample.csv') as f:
    for idx, line in enumerate(f):
        #print(line.split(",")[6],end="")
        #print("*"*6)
        gender = (line.split(",")[5]).rstrip("\n")
        amount = float ((line.split(",")[6]).rstrip("\n"))
        if gender == "Men":
            totalmen.append(amount)
        elif gender == "Women":
            totalwomen.append(amount)
        elif gender  == "Kid":
            totalkid.append(amount)
        elif gender == "Infant":
            totalinfant.append(amount)
        elif gender == "Unisex":
            totalunisex.append(amount)
        else:
            totalother.append(amount)
    if  sum(totalmen) != 0:
        print( "Average men price is ", round(sum(totalmen)/len(totalmen),2))
    if  sum(totalwomen) != 0:
        print( "Average women price is ", round(sum(totalwomen)/len(totalwomen),2))
    if  sum(totalkid) != 0:
        print( "Average kid price is ", round(sum(totalkid)/len(totalkid),2))
    if  sum(totalinfant) != 0:
        print( "Average infant price is ", round(sum(totalinfant)/len(totalinfant),2))
    if  sum(totalother) != 0:
        print( "Average other price is ", sum(totalother)/len(totalother))
    if  sum(totalunisex) != 0:
        print( "Average unisex price is ", sum(totalunisex)/len(totalunisex))




#
# with open('C:/Users/lranchev.BOS-WPTSD/Desktop/catalog_full.csv') as f2:
#     for line in f2:
#         total.append(float ((line.split(",")[6]).rstrip("\n")))
#     print (sum(total)/len(total))
