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
    ret = []
    for posizione_da_cui_partire in range(len(testo_originale)):
        print(f"posizione_da_cui_partire:{posizione_da_cui_partire}")
        if testo_originale[posizione_da_cui_partire].isdigit():
            print(f"La {posizione_da_cui_partire}-sima lettera e' {testo_originale[posizione_da_cui_partire]} ed e' un NUMERO!!!")
            ret.append(testo_originale[posizione_da_cui_partire])
        
    return ''.join(ret)


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

        restituito_1 = scambia_numero(linea, 'one', '1')
        print(f"restituito_1:{restituito_1}")
        estratto_1 = estrai_numero(linea, 'one', '1')
        print(f"estratto_1:{estratto_1}")
        restituito_2 = scambia_numero(linea, 'two', '2')
        print(f"restituito_2:{restituito_2}")

    
    #risultati=re.findall(r"(one|1))", linea)
    #for trovato in risultati:
    #    print(f"Ho trovato:{trovato}")

        prima_cifra = None
        ultima_cifra = None
        numero = None
        for carattere in linea:
        #print("[" + carattere + "]")
            if sei_un_numero(carattere):
                if prima_cifra==None:
                    prima_cifra=carattere
                ultima_cifra=carattere
        #print("prima_cifra:" + str(prima_cifra))
        #print("ultima_cifra:" + str(ultima_cifra))
    #print("Fine linea")
    #numero = int(prima_cifra + ultima_cifra)
    #print (numero)
    #totale += numero
    print (totale)



if __name__ == "__main__":
    main()

