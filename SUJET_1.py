##Question 1 : 

tab = [(12,14,20), (12,34,56), "Ultrasonic"]
def ajout(type):
    tab.append(type)
#ajout(15)
#print(f"Date : {tab[0]}, Heure : {tab[1]}, Type : {tab[2]}, distance : {tab[3]}")

##Question 2 : 

tab = []
def ajout_ordre(date, temps, typ, capteur):
    if date == None or temps == None or typ == None or capteur == None:
        return("Tableau vide")
    else:
        tab.append([date, temps, typ, capteur])
#ajout_ordre((12,1,19), (12,45,23), "distance", "ultrasonic")
#print(f"Date : {tab[0][0]}, Heure : {tab[0][1]}, Type : {tab[0][2]}, Distance : {tab[0][3]}")

##Question 3 : 

tab = [["12-14-56", "15-44-23", "46", "Ultrasonic"],
       ["19-13-22", "19-43-56", "33", "Ultrasonic"],
       ["13-33-21", "16-34-44", "98", "Ultrasonic"],
       ["07-33-45", "21-23-29", "98", "Ultrasonic"]]
def implementation():
    searched_ID = int(input("Entrez l'ID recherché : "))
    ID = []
    for liste in tab:
        if str(searched_ID) in liste:
            ID.append(liste)
    if ID:
        for item in ID:
            print("\t".join(item))
            print()
    else:
        return f"L'ID {searched_ID} n'existe pas dans ce tableau"
#implementation()

##Question 4 : 

tab = [["12-14-56", "15-44-23", "46", "Ultrasonic"],
       ["19-13-22", "19-43-56", "33", "Ultrasonic"],
       ["13-33-21", "16-34-44", "98", "Ultrasonic"],
       ["07-33-45", "21-23-29", "98", "Ultrasonic"]]


def criteres():
    searched_id = int(input("Entrez l'ID recherché : "))
    heure_min = str(input("De l'heure : "))
    heure_max = str(input("Jusqu'à l'heure : "))
    ID = []
    for liste in tab:
        if str(searched_id) in liste and liste[0] >= str(heure_min) and liste[1] <= str(heure_max):
            ID.append(liste)
    if ID:
        for item in ID:
            print("\t".join(item))
            print()
    else:
        print(f"Il n'y a pas d'ID {searched_id} dans l'intervalle {heure_min}, {heure_max}")
#criteres()

##Question 5 : 

tab = [["12-14-56", "15-44-23", "46", "Ultrasonic"],
       ["19-13-22", "19-43-56", "33", "Ultrasonic"],
       ["13-33-21", "16-34-44", "98", "Ultrasonic"],
       ["07-33-45", "21-23-29", "98", "Ultrasonic"]]


def tri_tableau(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range(i+1, len(tab)):
            date_i = tab[i][0]
            date_j = tab[j][0]
            if date_j < date_i:
                min_index = j
               
        tab[i], tab[min_index] = tab[min_index], tab[i]
#tri_tableau(tab)
for ligne in tab:
    print("\t".join(ligne))
    print()

##Question 6 : 

tab = [["12-14-56", "15-44-23", "46", "Ultrasonic"],
       ["19-13-22", "19-43-56", "33", "Ultrasonic"],
       ["13-33-21", "16-34-44", "98", "Ultrasonic"],
       ["07-33-45", "21-23-29", "98", "Ultrasonic"]]


def implementation():
    searched_ID = int(input("Entrez l'ID recherché : "))
    ID = []
    for liste in tab:
        if str(searched_ID) in liste:
            ID.append(liste)
    if ID:
        for item in ID:
            print("\t".join(item))
            print()
    else:
        print(f"L'ID {searched_ID} n'existe pas dans ce tableau")
       
def tri_tableau(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range(i+1, len(tab)):
            date_i = tab[i][0]
            date_j = tab[j][0]
            if date_j < date_i:
                min_index = j
               
        tab[i], tab[min_index] = tab[min_index], tab[i]
       
    for ligne in tab:
        print("\t".join(ligne))
        print()
       
def criteres():
    searched_id = int(input("Entrez l'ID recherché : "))
    heure_min = str(input("De l'heure : "))
    heure_max = str(input("Jusqu'à l'heure : "))
    ID = []
    for liste in tab:
        if str(searched_id) in liste and liste[0] >= str(heure_min) and liste[1] <= str(heure_max):
            ID.append(liste)
    if ID:
        for item in ID:
            print("\t".join(item))
            print()
    else:
        print(f"Il n'y a pas d'ID {searched_id} dans l'intervalle {heure_min}, {heure_max}")


#print("Choisissez l'un des trois paramètres : Identifiant, IntervalleTemps ou OrdreChrono")
#choix = input()


if choix == "Identifiant":
    implementation()
   
elif choix == "OrdreChrono":
    tri_tableau(tab)
   
elif choix == "IntervalleTemps":
    criteres()
   
else:
    print(f"Il n'y a pas de paramètre se nommant {choix}")
