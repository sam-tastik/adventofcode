import sys

def sei_un_numero(carattere):
    if carattere == '1' or carattere == '2' or carattere == '3' or carattere == '4' or carattere == '5' or carattere == '6' or carattere == '7' or carattere == '8' or carattere == '9' or carattere == '0':
        return True
    else:
        return False

def sei_un_iniziale_numero(carattere):
    if carattere == 'o' or carattere == 't' or carattere == 'f' or carattere == 's' or carattere == 'e' or carattere == 'n' or carattere == 'z':
        return True
    else:
        return False

def scambia_numero(testo, numero_in_lettere, numero_in_cifre):
    if numero_in_lettere in testo:
        print(f"Ho trovato la parola '{numero_in_lettere}'")
        nuova_linea = testo.replace(numero_in_lettere, numero_in_cifre)
        print(f"testo:{testo.strip()}  --> nuova_linea:{nuova_linea.strip()}")
        return nuova_linea
    else:
        print(f"Non ho trovato la parola '{numero_in_lettere}'")
        return None

def estrai_numero(testo, numero_in_lettere, numero_in_cifre):
    if numero_in_lettere in testo:
        return numero_in_cifre
    else:
        return None

def trasforma_riga(testo_originale):
    print(f"testo_originale:{testo_originale}")
    
    # prepara una variabile dove salvare il risultato
    tradotto = ''

    for posizione, lettera in enumerate(testo_originale):
        if lettera.isdigit():
            #print(f"La lettera '{lettera}' ed e' un NUMERO!!!")
            tradotto += lettera
        elif testo_originale[posizione:posizione+len('one')] == 'one':
            #print("Qui 'one'")
            tradotto +=  '1'
        elif testo_originale[posizione:posizione+len('two')] == 'two':
            #print("Qui 'two'")
            tradotto +=  '2'
        elif testo_originale[posizione:posizione+len('three')] == 'three':
            #print("Qui 'three'")
            tradotto +=  '3'
        elif testo_originale[posizione:posizione+len('four')] == 'four':
            #print("Qui 'four'")
            tradotto +=  '4'
        elif testo_originale[posizione:posizione+len('five')] == 'five':
            #print("Qui 'five'")
            tradotto +=  '5'
        elif testo_originale[posizione:posizione+len('six')] == 'six':
            #print("Qui 'six'")
            tradotto +=  '6'
        elif testo_originale[posizione:posizione+len('seven')] == 'seven':
            #print("Qui 'seven'")
            tradotto +=  '7'
        elif testo_originale[posizione:posizione+len('eight')] == 'eight':
            #print("Qui 'eight'")
            tradotto +=  '8'
        elif testo_originale[posizione:posizione+len('nine')] == 'nine':
            #print("Qui 'nine'")
            tradotto +=  '9'
        #else:
            #print(f"Qui qualcosa altro --> testo_originale[{posizione}:]={testo_originale[posizione:]}")

    print(f"tradotto={tradotto}")
    
    # Ritorna il risultato finale
    return tradotto


def main():
    print("Ciao a tutti")
    print("SYS:ARG -->  " + sys.argv[1])
    nome_diario =  sys.argv[1]

    f = open(nome_diario, 'r', encoding='utf-8')
    contenuto = f.readlines()
    contenuto_modificato = []
    totale = 0
    for linea in contenuto:
        print('-' * 30)
        print(linea.strip())

        tradotto = trasforma_riga(linea.strip())
        prima_cifra = None
        ultima_cifra = None
        numero = None
        for carattere in tradotto:
            print("[" + tradotto + "]")
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



if __name__ == "__main__":
    main()

