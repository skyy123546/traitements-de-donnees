##Question 1:

tab1 = [["Durand", "Jean", "Homme", "17-06-2011"],
        ["Dupont", "Jeanne", "Femme", "11-01-2004"],
        ["Durand", "Marie", "Femme", "23-04-1986"],
        ["Durand", "Charles", "Homme", "17-12-1986"],
        ["Dupont", "Richard", "Homme", "29-08-1979"],
        ["Dupont", "Anne", "Femme", "22-09-1979"]]


def ajout_ligne():
    ajout_de_lignes = ["Dumont", "Patrick", "Homme", "11-10-2006"]
    for row in tab1:
        tab_tab = print("\t".join(row))
    tab_ajout_de_lignes = print("\t".join(ajout_de_lignes))
    return(tab_tab, tab_ajout_de_lignes)
       
#ajout_ligne()

##Question 2:

tab1 = [["Durand", "Jean", "Homme", "17-06-2011"],
        ["Dupont", "Jeanne", "Femme", "11-01-2004"],
        ["Durand", "Marie", "Femme", "23-04-1986"],
        ["Durand", "Charles", "Homme", "17-12-1986"],
        ["Dupont", "Richard", "Homme", "29-08-1979"],
        ["Dupont", "Anne", "Femme", "22-09-1979"]]


def ordre_enregistrement():
    ordre = ["1", "2", "3", "4", "5", "6"]
    for row, value in zip(tab1, ordre):
        row.append(value)
    for row in tab1:
        tab_tab = print("\t".join(row))  
    return(tab_tab)
       
#ordre_enregistrement()

##Question 3:

new_tab1 = [["Durand", "Jean", "Homme", "17-06-2011", "1"],
        ["Dupont", "Jeanne", "Femme", "11-01-2004", "2"],
        ["Durand", "Marie", "Femme", "23-04-1986", "3"],
        ["Durand", "Charles", "Homme", "17-12-1986", "4"],
        ["Dupont", "Richard", "Homme", "29-08-1979", "5"],
        ["Dupont", "Anne", "Femme", "22-09-1979", "6"]]


def selection_num():
    numero = int(input("Entrez un numéro (entre 1 et 6 sinon bagarre) : "))
    num = []
    for liste in new_tab1:
        if str(numero) in liste:
            num.append(liste)
           
    if num:
        for item in num:
            print("\t".join(item))
            print()
    else:
        print(f"Le numéro {numero} ne se trouve pas dans le tableau (tu cherches la merde)")
       
#selection_num()

##Question 4:

new_tab1 = [["Durand", "Jean", "Homme", "17-06-2011", "1"],
        ["Dupont", "Jeanne", "Femme", "11-01-2004", "2"],
        ["Durand", "Marie", "Femme", "23-04-1986", "3"],
        ["Durand", "Charles", "Homme", "17-12-1986", "4"],
        ["Dupont", "Richard", "Homme", "29-08-1979", "5"],
        ["Dupont", "Anne", "Femme", "22-09-1979", "6"]]
humain1 = int(input("Entrez le numéro de l'enfant : "))
humain2 = int(input("Entrez le numéro du père ou de la mère : "))
def lien_parenté():
    global humain1, humain2, sexe_humain2, sexe_humain1
    tab2 = []
    p1 = []
    for liste in new_tab1:
        if str(humain1) in liste:
            p1.append(liste[1])      
    personne1 = p1
    for value in personne1:
        tab2.append(value)  
    p2 = []
    for liste in new_tab1:
        if str(humain2) in liste:
            p2.append(liste[1])   
    personne2 = p2
    for value in personne2:
        tab2.append(value) 
    for liste in new_tab1:
        if liste[4] == str(humain1):
            sexe_humain1 = liste[2]     
    for liste in new_tab1:
        if liste[4] == str(humain2):
            sexe_humain2 = liste[2]
    if sexe_humain1 == "Homme":
        if sexe_humain2 == "Homme":
            lien_de_parenté = "Pere et fils"
        else:
            lien_de_parenté = "Mere et fils"
    else:
        if sexe_humain2 == "Homme":
            lien_de_parenté = "Pere et fille"
        else:
            lien_de_parenté = "Mere et fille"     
    tab2.append(lien_de_parenté)
    tab_tab2 = print("\t".join(tab2))
    return(tab_tab2)
#lien_parenté()

##Question 5:

new_tab1 = [["Durand", "Jean", "Homme", "17-06-2011", "1"],
        ["Dupont", "Jeanne", "Femme", "11-01-2004", "2"],
        ["Durand", "Marie", "Femme", "23-04-1986", "3"],
        ["Durand", "Charles", "Homme", "17-12-1986", "4"],
        ["Dupont", "Richard", "Homme", "29-08-1979", "5"],
        ["Dupont", "Anne", "Femme", "22-09-1979", "6"]]


enfant = int(input("Entrer le numéro de l'enfant : "))
def ascendant():
    global enfant
    noms_famille = []
    for liste in new_tab1:
        if liste[4] == str(enfant):
            noms_famille.append(liste[0])
   
    numeros = []
    for nom in noms_famille:
        for liste in new_tab1:
            if liste[0] == nom:
                numeros.append(liste[4])


    tab2 = print("\t".join(numeros))
    return(tab2)


#ascendant()

##Question 6:

new_tab1 = [["Durand", "Jean", "Homme", "17-06-2011", "1"],
        ["Dupont", "Jeanne", "Femme", "11-01-2004", "2"],
        ["Durand", "Marie", "Femme", "23-04-1986", "3"],
        ["Durand", "Charles", "Homme", "17-12-1986", "4"],
        ["Dupont", "Richard", "Homme", "29-08-1979", "5"],
        ["Dupont", "Anne", "Femme", "22-09-1979", "6"]]


pere = int(input("Entrez le numéro du père : "))
mere = int(input("Entrez le numéro de la mère : "))


def descendant():
    global pere, mere
    noms_parents = set()
    tab2 = set()
   
    for liste in new_tab1:
        if liste[4] == str(pere) or liste[4] == str(mere):
            noms_parents.add(liste[0])
            tab2.add(liste[4])
           
    for liste in new_tab1:
        if liste[0] in noms_parents and liste[4] != str(pere) and liste[4] != str(mere):
            tab2.add(liste[4])
           
    tab_tab2 = print("\t".join(tab2))
    return(tab_tab2)


#descendant()

##Question 7:

from datetime import datetime


new_tab1 = [["Durand", "Jean", "Homme", "2011-06-17", "1"],
            ["Dupont", "Jeanne", "Femme", "2004-01-11", "2"],
            ["Durand", "Marie", "Femme", "1986-04-01", "3"],
            ["Durand", "Charles", "Homme", "1986-12-17", "4"],
            ["Dupont", "Richard", "Homme", "1979-08-12", "5"],
            ["Dupont", "Anne", "Femme", "1979-09-22", "6"],
            ["Durand", "Luc", "Homme", "2009-12-22", "7"],
            ["Durand", "Louise", "Femme", "2007-02-25", "8"],
            ["Dupont", "Louis", "Homme", "2006-11-24", "9"],
            ["Dupont", "Marine", "Femme", "2002-05-19", "10"]]


personne = int(input("Entrez le numéro de la personne : "))
DateL = None
dateN = "2000-01-01"
dateM = datetime.strptime(dateN, "%Y-%m-%d")
def freres_soeurs():
    global personne, DateL, dateN, dateM
    tab2 = set()
    freres_et_soeurs = set()
   
    for liste in new_tab1:
        if liste[4] == str(personne):
            freres_et_soeurs.add(liste[0])
            DateL = datetime.strptime(liste[3], "%Y-%m-%d")
           
    for liste in new_tab1:
        if liste[0] in freres_et_soeurs:
            date_naissance = datetime.strptime(liste[3], "%Y-%m-%d")
            if date_naissance > dateM and liste[4] != str(personne):
                tab2.add(liste[4])
           
    tab_tab2 = print("\t".join(tab2))
    return(tab_tab2)
#freres_soeurs()

##Question 8:

new_tab1 = [["Durand", "Jean", "Homme", "2011-06-17", "1"],
            ["Dupont", "Jeanne", "Femme", "2004-01-11", "2"],
            ["Durand", "Marie", "Femme", "1986-04-01", "3"],
            ["Durand", "Charles", "Homme", "1986-12-17", "4"],
            ["Dupont", "Richard", "Homme", "1979-08-12", "5"],
            ["Dupont", "Anne", "Femme", "1979-09-22", "6"],
            ["Durand", "Luc", "Homme", "2009-12-22", "7"],
            ["Durand", "Louise", "Femme", "2007-02-25", "8"],
            ["Dupont", "Louis", "Homme", "2006-11-24", "9"],
            ["Dupont", "Marine", "Femme", "2002-05-19", "10"]]
 
def tri():
    tab2 = []
    for i in range(len(new_tab1)):
        a = min(new_tab1)
        c = new_tab1.index(a)
        tab2.append(new_tab1[c])
        new_tab1.remove(a)
       
    for liste in tab2:
        print("\t".join(liste))
        print()
#tri()

##Question 9:

new_tab1 = [["Durand", "Jean", "Homme", "2011-06-17", "1", "12"],
            ["Dupont", "Jeanne", "Femme", "2004-01-11", "2", "20"],
            ["Durand", "Marie", "Femme", "1986-04-01", "3", "33"],
            ["Durand", "Charles", "Homme", "1986-12-17", "4", "33"],
            ["Dupont", "Richard", "Homme", "1979-08-12", "5", "41"],
            ["Dupont", "Anne", "Femme", "1979-09-22", "6", "41"],
            ["Durand", "Luc", "Homme", "2009-12-22", "7", "14"],
            ["Durand", "Louise", "Femme", "2007-02-25", "8", "17"],
            ["Dupont", "Louis", "Homme", "2006-11-24", "9", "17"],
            ["Dupont", "Marine", "Femme", "2002-05-19", "10", "21"]]


def tri_tableau():
    global new_tab1
    for j in range(len(new_tab1)):
        min_index = j
        for i in range(j+1, len(new_tab1)):
            age_i = str(new_tab1[i][5])
            age_j = str(new_tab1[min_index][5])
            if age_j < age_i:
                min_index = i
               
        new_tab1[min_index], new_tab1[j] = new_tab1[j], new_tab1[min_index]


#tri_tableau()
for liste in new_tab1:
    print("\t".join(liste))
    print()

##Question 10:

from datetime import datetime


new_tab1 = [["Durand", "Jean", "Homme", "2011-06-17", "1", "12"],
            ["Dupont", "Jeanne", "Femme", "2004-01-11", "2", "20"],
            ["Durand", "Marie", "Femme", "1986-04-01", "3", "33"],
            ["Durand", "Charles", "Homme", "1986-12-17", "4", "33"],
            ["Dupont", "Richard", "Homme", "1979-08-12", "5", "41"],
            ["Dupont", "Anne", "Femme", "1979-09-22", "6", "41"],
            ["Durand", "Luc", "Homme", "2009-12-22", "7", "14"],
            ["Durand", "Louise", "Femme", "2007-02-25", "8", "17"],
            ["Dupont", "Louis", "Homme", "2006-11-24", "9", "17"],
            ["Dupont", "Marine", "Femme", "2002-05-19", "10", "21"]]


def selection_num():
    numero = int(input("Entrez un numéro (entre 1 et 6 sinon bagarre) : "))
    num = []
    for liste in new_tab1:
        if str(numero) in liste:
            num.append(liste)
           
    if num:
        for item in num:
            print("\t".join(item))
            print()
    else:
        print(f"Le numéro {numero} ne se trouve pas dans le tableau (tu cherches la merde)")


def lien_parenté():
    humain1 = int(input("Entrez le numéro de l'enfant : "))
    humain2 = int(input("Entrez le numéro du père ou de la mère : "))
    tab2 = []
   
    p1 = []
    for liste in new_tab1:
        if str(humain1) in liste:
            p1.append(liste[1])
           
    personne1 = p1
    for value in personne1:
        tab2.append(value)
       
    p2 = []
    for liste in new_tab1:
        if str(humain2) in liste:
            p2.append(liste[1])
           
    personne2 = p2
    for value in personne2:
        tab2.append(value)
       
    for liste in new_tab1:
        if liste[4] == str(humain1):
            sexe_humain1 = liste[2]
           
    for liste in new_tab1:
        if liste[4] == str(humain2):
            sexe_humain2 = liste[2]


    if sexe_humain1 == "Homme":
        if sexe_humain2 == "Homme":
            lien_de_parenté = "Pere et fils"
        else:
            lien_de_parenté = "Mere et fils"
    else:
        if sexe_humain2 == "Homme":
            lien_de_parenté = "Pere et fille"
        else:
            lien_de_parenté = "Mere et fille"
               
    tab2.append(lien_de_parenté)
   
    tab_tab2 = print("\t".join(tab2))
    return(tab_tab2)
   
def ascendant():
    personne = int(input("Entrez le numéro de l'enfant : "))
    DateL = None
    dateN = "2000-01-01"
    dateM = datetime.strptime(dateN, "%Y-%m-%d")
    tab2 = set()
    parents = set()
   
    for liste in new_tab1:
        if liste[4] == str(personne):
            parents.add(liste[0])
            DateL = datetime.strptime(liste[3], "%Y-%m-%d")
           
    for liste in new_tab1:
        if liste[0] in parents:
            date_naissance = datetime.strptime(liste[3], "%Y-%m-%d")
            if date_naissance < dateM and liste[4] != str(personne):
                tab2.add(liste[4])
           
    tab_tab2 = print("\t".join(tab2))
    return(tab_tab2)  


def descendant():
    père = int(input("Entrez le numéro du père : "))
    mère = int(input("Entrez le numéro de la mère : "))
    DateL = None
    dateN = "2000-01-01"
    dateM = datetime.strptime(dateN, "%Y-%m-%d")
    tab2 = set()
    parents = set()
   
    for liste in new_tab1:
        if liste[4] == str(père) and str(mère):
            parents.add(liste[0])
            DateL = datetime.strptime(liste[3], "%Y-%m-%d")
           
    for liste in new_tab1:
        if liste[0] in parents:
            date_naissance = datetime.strptime(liste[3], "%Y-%m-%d")
            if date_naissance > dateM and liste[4] != str(père) and liste[4] != str(mère):
                tab2.add(liste[4])
           
    tab_tab2 = print("\t".join(tab2))
    return(tab_tab2)


   
def freres_soeurs():
    personne = int(input("Entrez le numéro de la personne : "))
    DateL = None
    dateN = "2000-01-01"
    dateM = datetime.strptime(dateN, "%Y-%m-%d")
    tab2 = set()
    freres_et_soeurs = set()
   
    for liste in new_tab1:
        if liste[4] == str(personne):
            freres_et_soeurs.add(liste[0])
            DateL = datetime.strptime(liste[3], "%Y-%m-%d")
           
    for liste in new_tab1:
        if liste[0] in freres_et_soeurs:
            date_naissance = datetime.strptime(liste[3], "%Y-%m-%d")
            if date_naissance > dateM and liste[4] != str(personne):
                tab2.add(liste[4])
           
    tab_tab2 = print("\t".join(tab2))
    return(tab_tab2)  
           
def tri():
    tab2 = []
    for i in range(len(new_tab1)):
        a = min(new_tab1)
        c = new_tab1.index(a)
        tab2.append(new_tab1[c])
        new_tab1.remove(a)
       
    for liste in tab2:
        print("\t".join(liste))
        print()
       
def tri_tableau():
    global new_tab1
    for j in range(len(new_tab1)):
        min_index = j
        for i in range(j+1, len(new_tab1)):
            age_i = str(new_tab1[i][5])
            age_j = str(new_tab1[min_index][5])
            if age_j < age_i:
                min_index = i
               
        new_tab1[min_index], new_tab1[j] = new_tab1[j], new_tab1[min_index]
    for liste in new_tab1:
        print("\t".join(liste))
        print()
   
       
print("paramètres disponibles : Numero, LienP, Ascendant, Descendant, FreresSoeurs, Tri_Nom, Tri_Age")
paramètre = input("Choisissez un paramètre parmi les précédents : ")


def paramètres():
    global paramètre
    if paramètre == "Numero":
        selection_num()
    elif paramètre == "LienP":
        lien_parenté()
    elif paramètre == "Ascendant":
        ascendant()
    elif paramètre == "Descendant":
        descendant()
    elif paramètre == "FreresSoeurs":
        freres_soeurs()
    elif paramètre == "Tri_Nom":
        tri()
    elif paramètre == "Tri_Age":
        tri_tableau()
    else:
        print(f"Il n'y a pas de paramètre nommé {paramètre}")
       
#paramètres()
