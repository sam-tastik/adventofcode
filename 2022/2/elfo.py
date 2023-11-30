import sys

print("Ciao a tutti")
print("SYS:ARG -->  " + sys.argv[1])
nome_diario =  sys.argv[1]

f = open(nome_diario, 'r', encoding='utf-8')
contenuto = f.readlines()

for linea in contenuto:
    print(linea)