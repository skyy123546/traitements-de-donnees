#####################################################################
# DEBUT DU SUJET 3 #
#####################################################################


# création de la classe Point !
import math
class Point:
# je définis a l'aide de mon construteurs les attributs de ma classe
# je définis x et y comme des attributs privés
def __init__(self, x, y):
self.__x = x
self.__y = y


# je définis les méthodes de ma classe
# ici mes attributs sont privés donc je ne peux pas les modifier directement
# je devrais passer par des décorateurs pour les modifier


#get
@property
def get_x(self):
return self.__x
@property
def get_y(self):
return self.__y


#set
@get_x.setter
def set_x(self, x):
self.__x = x
@get_y.setter
def set_y(self, y):
self.__y = y
def __str__(self):
return f"({int(self.__x)}, {int(self.__y)})"




i = Point(1, 2)
print(i.get_x, i.get_y)
i.set_x, i.set_y = 3, 4
print(i.get_x, i.get_y)


#création de la class segment:


class Segment:
def __init__(self, pt1, pt2):
self.__point1 = pt1
self.__point2 = pt2
def centre(self):
x = (self.__point1.get_x + self.__point2.get_x) / 2
y = (self.__point1.get_y + self.__point2.get_y) / 2
return Point(x, y)
def longueur(self):
x1 = self.__point1.get_x**2
x2 = self.__point2.get_x**2
y1 = self.__point1.get_y**2
y2 = self.__point2.get_y**2
resultat = math.sqrt((x2 - x1) + (y2 - y1))
return resultat


l = Segment(Point(1, 2), Point(3, 4))
centres = l.centre()
print(centres)
hjg = l.longueur()
print(hjg)


# création de la class Polygon
# points est une liste de points
# au début vide
class Polygon:
def __init__(self, points):
self.__points = points
def ajouterPoint(self, point):
self.__points.append(point)
def perimetre(self):
perimetre = 0
for i in range(len(self.__points) - 1):
perimetre += math.sqrt((self.__points[i+1].get_x - self.__points[i].get_x)**2 + (self.__points[i+1].get_y - self.__points[i].get_y)**2)
return perimetre
def __str__(self):
string = ""
for point in self.__points:
string += str(point) + "\n"
return string
f = Polygon([])
f.ajouterPoint(Point(1, 2))
f.ajouterPoint(Point(3, 4))
f.ajouterPoint(Point(5, 6))
print(f.perimetre())
print(f)


#####################################################################
# FIN DU SUJET 3 #
#####################################################################
