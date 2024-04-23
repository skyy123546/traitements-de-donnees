import requests
import time

#############################################################################
##              programme de base pour le traitement de données            ##
#############################################################################
import time
def traitement_de_donnees(log_file_path = "emplacement fichier"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                ip, identd, user, date, utc, method, url, protocol, code, size = parts[:10]
                print(f"IP: {ip} {nl} Date: {date}{nl} UTC: {utc}{nl} method: {method}{nl} Url: {url}{nl} Protocol: {protocol},{nl} Code: {code},{nl} size: {size}")
                time.sleep(15)  # import time
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
#traitement_de_donnees()   """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""
#############################################################################
##              programme pour trouver la taille max d'un log              ##
#############################################################################
def taille_max(log_file_path = "emplacement fichier log"):
    tab = []
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if not len(parts) in tab:
                tab.append(len(parts))
            else :
                pass
    print(max(tab))
   
#taille_max()  """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


#############################################################################
##              programme pour avoir la liste des Ip                       ##
#############################################################################
tab = []
def ip(log_file_path = "emplacement fichier log"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                if not parts[0] in tab:
                    tab.append(parts[0])
                else :
                    pass
    print(tab)
#ip()  """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


#############################################################################
##  programme pour avoir la liste des ip en fonctions de la taille de log  ##
#############################################################################


tab = []
def ip_taille(log_file_path = "emplacement fichier log", taille = 28):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == taille:
                if not parts[0] in tab:
                    tab.append(parts[0])
                else :
                    pass
    print(tab)
#ip_taille()   """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


#############################################################################
##               infos sur les ip a l'aide d'une api                       ##
#############################################################################


# Fonction pour géolocaliser une adresse IP en utilisant l'API ip-api.com
def getIP_infos(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    time.sleep(1.5)  # Pause pour respecter la limite de requêtes de l'API
    return data


# Fonction pour lire le fichier de logs Apache, extraire les adresses IP et les géolocaliser
def traitement_de_donnees(log_file_path = "emplacement fichier log"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                ip, identd, user, timestamp, request, status, size, referer, user_agent = parts[0]
                ip_address = ip
                # Géolocaliser l'adresse IP
                data = getIP_infos(ip_address)
                nl = "\n"
                print(f'IP: {ip_address},{nl} Pays: {data["country"]},{nl} Ville: {data["city"]},{nl} ISP: {data["isp"]},{nl} Latitude: {data["lat"]},{nl} Longitude: {data["lon"]}')


# Appeler la fonction de traitement de données
#traitement_de_donnees()  """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


#############################################################################
##      programme qui ressort des courbes en fonction des données          ##
#############################################################################


import requests
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime


def courbes(log_file_path = "emplacement fichier log"):
    # Initialiser un dictionnaire pour compter le nombre de requêtes par date
    requetes_par_date = defaultdict(int)


    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                timestamp = parts[3][1:]  # Supprimer le premier caractère '['
                date = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")  # Convertir la chaîne de caractères en date
                requetes_par_date[date.date()] += 1  # Incrémenter le compteur pour cette date


    # Créer une liste de dates et une liste de nombres de requêtes
    dates = sorted(requetes_par_date.keys())
    requetes = [requetes_par_date[date] for date in dates]


    # Créer un graphique
    plt.plot(dates, requetes)
    plt.xlabel('Date')
    plt.ylabel('Nombre de requêtes')
    plt.title('Nombre de requêtes par date')
    plt.show()


# Appeler la fonction de traitement de données
#courbes()  """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


#############################################################################
##      programme qui ressort l'os et la version et dénombrement           ##
#############################################################################


import time
def ostqt(log_file_path = "emplacement fichier log"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                os = parts[12:17]
                print(f"Os: {os}.")
                #time.sleep()  # import time
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
#ostqt()  """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


#############################################################################
##    programme qui ressort le navigateur et la version et dénombrement    ##
#############################################################################


import time
def navtqt(log_file_path = "emplacement fichier log"):
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                nav = parts[11:12]
                nav2 = parts[20:21]
                nav3 = parts[22:23]
                if "Mozilla/5.0" in nav or "Firefox" in nav2 or "Chrome/95.0.4638.74" in nav2 or "Safari/537.36" in nav3:
                    print(f"nav: {nav} & {nav2} & {nav3}.")
                #time.sleep()  # import time
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
               
#navtqt()  """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""




#############################################################################
##              programme qui ressort le nombre d'erreur http              ##
#############################################################################
tab = []
a, b, c, d, e, f, g, h, i, j = ['200'], ['301'], ['400'], ['304'], ['500'], ['302'], ['404'], ['206'], ['401'], ['403']
A1 = B1 = C1 = D1 = E1 = F1 = G1 = H1 = I1 = J1 = 0
import time
def http(log_file_path = "emplacement fichier log"):
   
    global A1, B1, C1, D1, E1, F1, G1, H1, I1, J1
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                nl = '\n'
                nav = parts[8:9]
                print(f"nombre d'erreur http: {nav}.")
                if nav == a :
                    A1 += 1
                if nav == b :
                    B1 += 1
                if nav == c :
                    C1 += 1
                if nav == d :
                    D1 += 1
                if nav == e :
                    E1 += 1
                if nav == f :
                    F1 += 1
                if nav == g :
                    G1 += 1
                if nav == h :
                    H1 += 1
                if nav == i :
                    I1 += 1
                if nav == j :
                    J1 += 1
               
                #time.sleep()  # import time
            else:
                print("La ligne du fichier de log ne correspond pas au format attendu.")
        print(f"{a} : {A1} {nl} {b} : {B1} {nl} {c} : {C1} {nl} {d} : {D1} {nl} {e} : {E1} {nl} {f} : {F1} {nl} {g} : {G1} {nl} {h} : {H1} {nl} {i} : {I1} {nl} {j} : {J1}")
               
#http()  """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


#################################################################################
#               Extrait la liste des commandes par jour à partir d'un fichier log
#               Entrée de la fonction : le fichier log (file)
#               Sortie de la fonction : la liste des commandes par jour (listdate)
##################################################################################


def gene_listdate(file ="emplacement fichier log") :
    f = open(file, "r")
    listdate=[]
    for ligne in f :
        a=ligne.split(" ")
        if len(a) == 28 and a not in listdate:
            listdate.append(a[3])
    return listdate


#print(gene_listdate()) """ ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


##############################################################################
##       FONCTION exportToJSONFile(liste) ENREG. DATA AU FORMAT JSON        ##
##############################################################################
import json
#ici nous devons définir un tableau qui contiendra d'autres tableaux
#[[ip, date, fuseau_horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...],
# [ip, date, fuseau_horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...],
# ... ]
"""tab = []
with open("emplacement fichier log", 'r') as file:
        for line in file:
            parts = line.split()
            tab.append(parts)


#print(tab)
a=tab       """
#Cette fonction demande en paramètre une liste de listes de données ici nommé a par le pregramme ci dessus
#Elle demande aussi un nom de fichier de destination
def exportToJSONFile(liste = a, fileNameDest = "fichier destination en json"):
    IP = 0
    DATE = 3
    UTC = 4             #on définit la position de chaque donnée dans la liste
    METHOD = 5
    URL = 6
    PROTOCOL = 7
    CODE = 8
    SIZE = 9
    DOMAIN = 10
    SYSTEM = 11
    ENGINE = 12
    BROWSER = 13


    json_log = []
    jsonTxt = '[\n'


    for i in range(len(liste)):
        if liste[i][IP] not in json_log and liste[i][IP] not in ["127.0.0.1"]:
            json_log.append(liste[i][IP])
            if len(liste[i]) >= 14:
                if i == 0:
                    jsonTxt += '{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code": "' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '", \n\t\t\t"domain": "' + str(
                        liste[i][DOMAIN]).replace('"', "") + '", \n\t\t\t"system": "' + str(
                        liste[i][SYSTEM]).replace('"', "") + '", \n\t\t\t"engine": "' + str(
                        liste[i][ENGINE]).replace('"', "") + '",\n\t\t\t"browser": "' + str(
                        liste[i][BROWSER]).replace('"', "") + '" }'
                else:
                    jsonTxt += ',{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code":" ' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '", \n\t\t\t"domain": "' + str(
                        liste[i][DOMAIN]).replace('"', "") + '", \n\t\t\t"system": "' + str(
                        liste[i][SYSTEM]).replace('"', "") + '", \n\t\t\t"engine": "' + str(
                        liste[i][ENGINE]).replace('"', "") + '", \n\t\t\t"browser": "' + str(
                        liste[i][BROWSER]).replace('"', "") + '" }'
            else:
                if i == 0:
                    jsonTxt += '{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code": "' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '" }'
                else:
                    jsonTxt += ',{\n\t\t\t"ip": "' + str(liste[i][IP]).replace('"', "") + '",\n\t\t\t"date": "' + str(
                        (liste[i][DATE])[1:len(liste[i][DATE])]).replace('"', "") + '", \n\t\t\t"fuseau_horaire":"' + str(
                        liste[i][UTC]).replace('"', "") + '", \n\t\t\t"method": "' + str(
                        liste[i][METHOD]).replace('"', "") + '", \n\t\t\t"url": "' + str(
                        liste[i][URL]).replace('"', "") + '", \n\t\t\t"protocol": "' + str(
                        liste[i][PROTOCOL]).replace('"', "") + '",  \n\t\t\t"return_code":" ' + str(
                        liste[i][CODE]).replace('"', "") + '", \n\t\t\t"size": "' + str(
                        liste[i][SIZE]).replace('"', "") + '" }'


        else:
            continue


    jsonTxt += "\n]"


    # Ecriture fichier GeoJson
    jsonFile = open(fileNameDest, "a")
    jsonFile.write(jsonTxt)
    jsonFile.close()
#exportToJSONFile() """ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser"""


##############################################################################
##        FONCTION exportToCSVFile(liste) ENREG. DATA AU FORMAT CSV         ##
##############################################################################
#ici nous devons définir un tableau qui contiendra d'autres tableaux
#[[ip, date, fuseau horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...],
# [ip, date, fuseau horaire, method, url, protocol, return_code, size, domain, system, engine, browser, ...],
# ... ]
tab = []
with open("emplacement fichier log", 'r') as file:
        for line in file:
            parts = line.split()
            tab.append(parts)


#print(tab)
a=tab[0:10]   #ici pour les test j'ai pris une petite partie des log car c'est long
              #mais si je veux tt il suffit de remplacer par a = tab[]


def exportToCSVFile(ipliste = a, fileNameDest = "fichier destination en csv"):
    csvContent = ""
    for i in range(len(ipliste)):
        for j in range(len(ipliste[i])):
            csvContent += '"' + str(ipliste[i][j]).replace('"', '""') + '",'
        csvContent = csvContent.rstrip(',') + "\n"  # Retirez la virgule à la fin de chaque ligne
   
    # Ecriture du fichier CSV
    with open(fileNameDest, "w") as csvFile:  # Utilisation de "w" pour créer un nouveau fichier
        csvFile.write(csvContent)
#exportToCSVFile() #ici on a un exemple d'utilisation de la fonction, il suffit de décommenter pour l'utiliser




##############################################################################
##      FONCTION exportToXMLFile(liste...) ENREG. DATA AU FORMAT XML        ##
##############################################################################




#################################################################################
#               Extrait toute les information d'un fichier log ( split " " )
#               Entrée de la fonction : le fichier log (file)
#               Sortie de la fonction : le fichier log split (data)
#               Utilité : permettre la conversion en XML , CSS et JSON
##################################################################################
def split(file):
    f = open(file, "r")
    data=[]
    for ligne in f:
        a=ligne.split(" ")
        data.append(a)
    return data


# on peut remplacer notre tab par data pour avoir le fichier log splité (dans nos programme)


##########################################################################
##       programme qui ressort la loc de l'ip dans un file html         ##
##########################################################################
import folium


# Fonction pour géolocaliser une adresse IP en utilisant l'API ip-api.com
def getIP_infos(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    time.sleep(1.5)  # Pause pour respecter la limite de requêtes de l'API
    return data


# Fonction pour lire le fichier de logs Apache, extraire les adresses IP et les géolocaliser
#le programme est bad long dcp j'ai créé un autre fichier log plus court log.log pour tester
def traitement_de_donnees(log_file_path = "ce qu'il y a marqué en vert"):
    tab1 = []
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                ip = parts[0]
                ip_address = ip
                # Géolocaliser l'adresse IP
                data = getIP_infos(ip_address)
                nl = "\n"
                print(f'IP: {ip_address},{nl} Pays: {data["country"]},{nl} Ville: {data["city"]},{nl} ISP: {data["isp"]},{nl} Latitude: {data["lat"]},{nl} Longitude: {data["lon"]}')
                tab1.append([ip_address, data["lat"], data["lon"]])
    return tab1
#décommenter pour utiliser le programme
"""aba = traitement_de_donnees()




#Créer une carte centrée sur les coordonnées GPS indiquée
carte= folium.Map(location=[43.920044, 5.051804])


for i in range(len(aba)):
    folium.Marker([aba[i][1], aba[i][2]],popup= aba[i][0],icon=folium.Icon(color='green')).add_to(carte)
#Sauvegarder cette carte dans un fichier HTML
carte.save('Carte1.html')"""
