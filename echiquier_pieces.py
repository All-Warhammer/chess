from colorama import*

Tou = [-8, +8, -1, +1]
Rei = [-9, -8, -7, -1, +1, +7, +8, +9]
Roi = [-9, -8, -7, -1, +1, +7, +8, +9]
Fou = [-7, -9, 7, 9]
Cav = [-17, -15, -10, -6, +6, +10, +15, +17]
Pion_B = [-8]
Pion_B_mange = [-7, -9]
Pion_N = [+8]
Pion_N_mange = [+7, +9]
Pion_N_debut = [+16]
Pion_B_debut = [-16]

No_color = Style.RESET_ALL
Alert_color = Fore.LIGHTWHITE_EX + Back.BLACK

Lettres = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8
}
Chiffre = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H"
}

Blanc = {
    "type": "Blanc",
    "couleur": Fore.RED,
    "Points": 0,
    "initiales": "_B",
    "mange": Pion_B_mange,
    "debut": Pion_B_debut,
    "normal": Pion_B,
    "Etat": True
}

Noir = {
    "type": "Noir",
    "couleur": Fore.BLUE,
    "Points": 0,
    "initiales": "_N",
    "Inverse": Blanc,
    "mange": Pion_N_mange,
    "debut": Pion_N_debut,
    "normal": Pion_N,
    "Etat": True
}

Blanc = {
    "type": "Blanc",
    "couleur": Fore.RED,
    "Points": 0,
    "initiales": "_B",
    "Inverse": Noir,
    "mange": Pion_B_mange,
    "debut": Pion_B_debut,
    "normal": Pion_B,
    "dico": Blanc,
    "Etat": True
}

Noir = {
    "type": "Noir",
    "couleur": Fore.BLUE,
    "Points": 0,
    "initiales": "_N",
    "Inverse": Blanc,
    "mange": Pion_N_mange,
    "debut": Pion_N_debut,
    "normal": Pion_N,
    "dico": Noir,
    "Etat": True
}

Tour = {
    "nom": "Tour",
    "Points": 5,
    "Initiales": " Tour",
    "deplacement": Tou
}
Cavalier = {
    "nom": "Cavalier",
    "Points": 3,
    "Initiales": "Caval",
    "deplacement": Cav
}
Fou = {
    "nom": "Fou",
    "Points": 3,
    "Initiales": " Fou ",
    "deplacement": Fou
}
Roi = {
    "nom": "Roi",
    "Points": 0,
    "Initiales": " Roi ",
    "deplacement": Roi
}
Reine = {
    "nom": "Reine",
    "Points": 9,
    "Initiales": "Reine",
    "deplacement": Rei
}
Pion = {
    "nom": "Pion",
    "Points": 1,
    "Initiales": " Pio "
}

Dico_pieces = {
    "Noir": Noir,
    "Blanc": Blanc,
    "Tour": Tour,
    "Cavalier": Cavalier,
    "Fou": Fou,
    "Roi": Roi,
    "Reine": Reine,
    "Pion": Pion
}

Image = {
    "Tour_Blanche": "image/tour_blanche.png",
    "Cavalier_Blanc": "image/cavalier_blanc.png",
    "Fou_Blanc": "image/fou_blanc.png",
    "Roi_Blanc": "image/roi_blanc.png",
    "Reine_Blanche": "image/reine_blanche.png",
    "Pion_Blanc": "image/pion_blanc.png",
    "Tour_Noir": "image/tour_noir.png",
    "Cavalier_Noir": "image/cavalier_noir.png",
    "Fou_Noir": "image/fou_noir.png",
    "Roi_Noir": "image/roi_noir.png",
    "Reine_Noir": "image/reine_noir.png",
    "Pion_Noir": "image/pion_noir.png"
}

Tour_Noir1 = {
    "nom": Tour["nom"],
    "type": Noir["type"],
    "image": Image["Tour_Noir"],
    "ligne": 1,
    "colonne": 1,
    "exligne": 1,
    "excolonne": 1,
    "couleur": Noir["couleur"],
    "deplacement": Tour["deplacement"]
}
Cavalier_Noir1 = {
    "nom": Cavalier["nom"],
    "type": Noir["type"],
    "image": Image["Cavalier_Noir"],
    "ligne": 1,
    "colonne": 2,
    "exligne": 1,
    "excolonne": 2,
    "couleur": Noir["couleur"],
    "deplacement": Cavalier["deplacement"]
}
Fou_Noir1 = {
    "nom": Fou["nom"],
    "type": Noir["type"],
    "image": Image["Fou_Noir"],
    "ligne": 1,
    "colonne": 3,
    "exligne": 1,
    "excolonne": 3,
    "couleur": Noir["couleur"],
    "deplacement": Fou["deplacement"]
}
Roi_Noir1 = {
    "nom": Roi["nom"],
    "type": Noir["type"],
    "image": Image["Roi_Noir"],
    "ligne": 1,
    "colonne": 5,
    "exligne": 1,
    "excolonne": 5,
    "couleur": Noir["couleur"],
    "deplacement": Roi["deplacement"]
}
Reine_Noir1 = {
    "nom": Reine["nom"],
    "type": Noir["type"],
    "image": Image["Reine_Noir"],
    "ligne": 1,
    "colonne": 4,
    "exligne": 1,
    "excolonne": 4,
    "couleur": Noir["couleur"],
    "deplacement": Reine["deplacement"]
}
Fou_Noir2 = {
    "nom": Fou["nom"],
    "type": Noir["type"],
    "image": Image["Fou_Noir"],
    "ligne": 1,
    "colonne": 6,
    "exligne": 1,
    "excolonne": 6,
    "couleur": Noir["couleur"],
    "deplacement": Fou["deplacement"]
}
Cavalier_Noir2 = {
    "nom": Cavalier["nom"],
    "type": Noir["type"],
    "image": Image["Cavalier_Noir"],
    "ligne": 1,
    "colonne": 7,
    "exligne": 1,
    "excolonne": 7,
    "couleur": Noir["couleur"],
    "deplacement": Cavalier["deplacement"]
}
Tour_Noir2 = {
    "nom": Tour["nom"],
    "type": Noir["type"],
    "image": Image["Tour_Noir"],
    "ligne": 1,
    "colonne": 8,
    "exligne": 1,
    "excolonne": 8,
    "couleur": Noir["couleur"],
    "deplacement": Tour["deplacement"]
}
Pion_Noir1 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 1,
    "exligne": 2,
    "excolonne": 1,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Pion_Noir2 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 2,
    "exligne": 2,
    "excolonne": 2,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Pion_Noir3 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 3,
    "exligne": 2,
    "excolonne": 3,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Pion_Noir4 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 4,
    "exligne": 2,
    "excolonne": 4,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Pion_Noir5 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 5,
    "exligne": 2,
    "excolonne": 5,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Pion_Noir6 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 6,
    "exligne": 2,
    "excolonne": 6,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Pion_Noir7 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 7,
    "exligne": 2,
    "excolonne": 7,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Pion_Noir8 = {
    "nom": Pion["nom"],
    "type": Noir["type"],
    "image": Image["Pion_Noir"],
    "ligne": 2,
    "colonne": 8,
    "exligne": 2,
    "excolonne": 8,
    "couleur": Noir["couleur"],
    "deplacement": Pion_N,
    "depart": 0
}
Tour_Blanc1 = {
    "nom": Tour["nom"],
    "type": Blanc["type"],
    "image": Image["Tour_Blanche"],
    "ligne": 8,
    "colonne": 1,
    "exligne": 8,
    "excolonne": 1,
    "couleur": Blanc["couleur"],
    "deplacement": Tour["deplacement"]
}
Cavalier_Blanc1 = {
    "nom": Cavalier["nom"],
    "type": Blanc["type"],
    "image": Image["Cavalier_Blanc"],
    "ligne": 8,
    "colonne": 2,
    "exligne": 8,
    "excolonne": 2,
    "couleur": Blanc["couleur"],
    "deplacement": Cavalier["deplacement"]
}
Fou_Blanc1 = {
    "nom": Fou["nom"],
    "type": Blanc["type"],
    "image": Image["Fou_Blanc"],
    "ligne": 8,
    "colonne": 3,
    "exligne": 8,
    "excolonne": 3,
    "couleur": Blanc["couleur"],
    "deplacement": Fou["deplacement"]
}
Roi_Blanc1 = {
    "nom": Roi["nom"],
    "type": Blanc["type"],
    "image": Image["Roi_Blanc"],
    "ligne": 8,
    "colonne": 5,
    "exligne": 8,
    "excolonne": 5,
    "couleur": Blanc["couleur"],
    "deplacement": Roi["deplacement"]
}
Reine_Blanc1 = {
    "nom": Reine["nom"],
    "type": Blanc["type"],
    "image": Image["Reine_Blanche"],
    "ligne": 8,
    "colonne": 4,
    "exligne": 8,
    "excolonne": 4,
    "couleur": Blanc["couleur"],
    "deplacement": Reine["deplacement"]
}
Fou_Blanc2 = {
    "nom": Fou["nom"],
    "type": Blanc["type"],
    "image": Image["Fou_Blanc"],
    "ligne": 8,
    "colonne": 6,
    "exligne": 8,
    "excolonne": 6,
    "couleur": Blanc["couleur"],
    "deplacement": Fou["deplacement"]
}
Cavalier_Blanc2 = {
    "nom": Cavalier["nom"],
    "type": Blanc["type"],
    "image": Image["Cavalier_Blanc"],
    "ligne": 8,
    "colonne": 7,
    "exligne": 8,
    "excolonne": 7,
    "couleur": Blanc["couleur"],
    "deplacement": Cavalier["deplacement"]
}
Tour_Blanc2 = {
    "nom": Tour["nom"],
    "type": Blanc["type"],
    "image": Image["Tour_Blanche"],
    "ligne": 8,
    "colonne": 8,
    "exligne": 8,
    "excolonne": 8,
    "couleur": Blanc["couleur"],
    "deplacement": Tour["deplacement"]
}
Pion_Blanc1 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 1,
    "exligne": 7,
    "excolonne": 1,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}
Pion_Blanc2 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 2,
    "exligne": 7,
    "excolonne": 2,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}
Pion_Blanc3 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 3,
    "exligne": 7,
    "excolonne": 3,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}
Pion_Blanc4 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 4,
    "exligne": 7,
    "excolonne": 4,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}
Pion_Blanc5 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 5,
    "exligne": 7,
    "excolonne": 5,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}
Pion_Blanc6 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 6,
    "exligne": 7,
    "excolonne": 6,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}
Pion_Blanc7 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 7,
    "exligne": 7,
    "excolonne": 7,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}
Pion_Blanc8 = {
    "nom": Pion["nom"],
    "type": Blanc["type"],
    "image": Image["Pion_Blanc"],
    "ligne": 7,
    "colonne": 8,
    "exligne": 7,
    "excolonne": 8,
    "couleur": Blanc["couleur"],
    "deplacement": Pion_B,
    "depart": 0
}



pieces = [Tour_Blanc1,Cavalier_Blanc1,Fou_Blanc1,Roi_Blanc1,Reine_Blanc1,Fou_Blanc2,Cavalier_Blanc2,Tour_Blanc2,Pion_Blanc1,Pion_Blanc2,Pion_Blanc3,Pion_Blanc4,Pion_Blanc5,Pion_Blanc6,Pion_Blanc7,Pion_Blanc8]
pieces += [Tour_Noir1,Cavalier_Noir1,Fou_Noir1,Roi_Noir1,Reine_Noir1,Fou_Noir2,Cavalier_Noir2,Tour_Noir2,Pion_Noir1,Pion_Noir2,Pion_Noir3,Pion_Noir4,Pion_Noir5,Pion_Noir6,Pion_Noir7,Pion_Noir8]

def echiquier():

    liste = []
    color_liste = []

    for i in range(64):
        liste += ["....."]
        color_liste += [Fore.BLACK]

    for i in range(len(pieces)):
        liste[emplacement(pieces[i])] = Dico_pieces[pieces[i]["nom"]]["Initiales"]
        color_liste[emplacement(pieces[i])] = pieces[i]["couleur"]

    print("           " + Back.LIGHTWHITE_EX +" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"+No_color)
    print("           "+Fore.BLACK+Back.LIGHTWHITE_EX+"|    A   |    B    |    C    |    D    |    E    |    F    |    G    |    H    |"+No_color)

    for i in range(8):
        if i == 0:
            print("  "+Back.LIGHTWHITE_EX+Fore.BLACK+" - - - - |- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |"+No_color)
        else:
            print("  "+Back.LIGHTWHITE_EX+"  _ _ _ _ "+No_color+"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print("  "+Fore.BLACK+Back.LIGHTWHITE_EX+" |___"+str(8-i)+"___|"+No_color+color_liste[i*8],liste[i*8],No_color,"|",color_liste[i*8+1],liste[i*8+1],No_color,"|",color_liste[i*8+2],liste[i*8+2],No_color,"|",color_liste[i*8+3],liste[i*8+3],No_color,"|",color_liste[i*8+4],liste[i*8+4],No_color,"|",color_liste[i*8+5],liste[i*8+5],No_color,"|",color_liste[i*8+6],liste[i*8+6],No_color,"|",color_liste[i*8+7],liste[i*8+7],No_color,"|",No_color)


def emplacement(piece):
    emplacement = (piece["ligne"]) * 8 + piece["colonne"] - 9
    return emplacement

def deplacement(ligne, colonne):
    deplacement = ligne * 8 + colonne - 9
    return deplacement

def deplacement_ligne(deplacement):
    ligne = abs((deplacement) // 8 +1)
    return ligne
def deplacement_colonne(deplacement):
    colonne = deplacement % 8 + 1
    return colonne

def deplacement_ligne_colonne(deplacement):
    ligne = abs((deplacement) // 8 +1)
    colonne = deplacement % 8 + 1
    return colonne, ligne

def emplacement_pieces(lieu, pieces):
    for o in range(len(pieces)):
        if int(emplacement(pieces[o])) == int(lieu):
            return True
        elif o == len(pieces)-1:
            return False
