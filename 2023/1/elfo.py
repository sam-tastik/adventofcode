import sys

def sei_un_numero(carattere):
    if carattere == '1' or carattere == '2' or carattere == '3' or carattere == '4' or carattere == '5' or carattere == '6' or carattere == '7' or carattere == '8' or carattere == '9' or carattere == '0':
        return True
    else:
        return False


print("Ciao a tutti")
print("SYS:ARG -->  " + sys.argv[1])
nome_diario =  sys.argv[1]

f = open(nome_diario, 'r', encoding='utf-8')
contenuto = f.readlines()
totale = 0
for linea in contenuto:
    print('-' * 30)
    print(linea.strip())
    prima_cifra = None
    ultima_cifra = None
    numero = None
    for carattere in linea:
        #print("[" + carattere + "]")
        if sei_un_numero(carattere):
            if prima_cifra==None:
                prima_cifra=carattere
            ultima_cifra=carattere
        print("prima_cifra:" + str(prima_cifra))
        print("ultima_cifra:" + str(ultima_cifra))
    print("Fine linea")
    numero = int(prima_cifra + ultima_cifra)
    print (numero)
    totale += numero
print (totale)

