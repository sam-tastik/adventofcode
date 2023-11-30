import sys

print("Ciao a tutti")
print("SYS:ARG -->  " + sys.argv[1])
#nome_diario = "diario_elfi.txt"
nome_diario =  sys.argv[1]

f = open(nome_diario, 'r', encoding='utf-8')
contenuto = f.readlines()

# cerco le calorie dello zaino con più calorie
calorie_di_un_elfo = 0
numero_massimo_calorie = 0
i_tre_con_piu_calorie = [0, 0, 0]
for linea in contenuto:
    if linea == '\n':
        # E' finito uno zaino
        if calorie_di_un_elfo > numero_massimo_calorie:
            # Questo zaino è quello con più calorie
            numero_massimo_calorie = calorie_di_un_elfo
        # resetto per prepararmi a contare le calorie del 
        # prossimo zaino
        calorie_di_un_elfo = 0
    else:
        # siamo dentro lo zaino, continuiamo a sommare le calorie
        calorie_di_un_elfo += int(linea)
# Arrivato qui so il mumero di calorie nello zaino che ne ha di più

# Cerco il numero di calorie del secondo zaino con più calorie
calorie_di_un_elfo = 0
numero_massimo_calorie2 = 0
for linea in contenuto:
    if linea == '\n':
        if calorie_di_un_elfo > numero_massimo_calorie2 and calorie_di_un_elfo < numero_massimo_calorie:
            numero_massimo_calorie2 = calorie_di_un_elfo
        calorie_di_un_elfo = 0
    else:
        calorie_di_un_elfo += int(linea)        

numero_elfi = 1
calorie_di_un_elfo = 0
numero_massimo_calorie3 = 0
i_tre_con_piu_calorie = [0, 0, 0]
for linea in contenuto:
    if linea == '\n':
        if calorie_di_un_elfo > numero_massimo_calorie3 and calorie_di_un_elfo < numero_massimo_calorie2:
            numero_massimo_calorie3 = calorie_di_un_elfo
        calorie_di_un_elfo = 0
    else:
        calorie_di_un_elfo += int(linea)

print(numero_massimo_calorie)
print(numero_massimo_calorie2)
print(numero_massimo_calorie3)