import sys
import math

input1 = "3,879483"
input2 = "43,608177"
input3 = "3"

input4 = [  "1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217",
            "2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849",
            "3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854"
        ]


lon = float(input1.replace(",", "."))
lat = float(input2.replace(",", "."))
n = int(input3)

defibs = []
for i in range(n):
    defib = input4[i].split(";")

    #convert from string to float
    lonB = defib[len(defib)-2] = float(defib[len(defib)-2].replace(",", "."))
    latB = defib[len(defib)-1] = float(defib[len(defib)-1].replace(",", "."))

    x = (lonB - lon) * math.cos((lat + latB)/2)
    y = latB - lat

    #convert to degrees
    x = (math.pi*x)/180
    y = (math.pi*y)/180

    d = math.sqrt(x*x + y*y) *6371

    defib.append(d)

    defibs.append(defib)

dist = None
answer = None
for i, places in enumerate(defibs):
    place_dist = places[len(places)-1]

    if dist is None:
        dist = place_dist
        answer = i
    else:
        if dist > place_dist:
            dist = place_dist
            answer = i

print(defibs[answer][1])
