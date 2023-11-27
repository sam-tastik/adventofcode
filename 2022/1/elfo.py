print("Ciao a tutti")

nome_diario = "diario_elfi.txt"

f = open(nome_diario, 'r')
contenuto = f.readlines()

numero_elfi = 1
calorie_di_un_elfo = 0
numero_massimo_calorie = 0
for linea in contenuto:
    if linea == '\n':
        numero_elfi = numero_elfi + 1
        print("Questo elfo aveva " + str(calorie_di_un_elfo) + " calorie.")
        if calorie_di_un_elfo > numero_massimo_calorie:
            numero_massimo_calorie = calorie_di_un_elfo
        calorie_di_un_elfo = 0
    else:
        calorie_di_un_elfo = calorie_di_un_elfo + int(linea)

print(numero_massimo_calorie)
