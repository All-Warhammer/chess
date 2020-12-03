from colorama import*
from echiquier_pieces import*
import pygame

pygame.init()

pygame.display.set_caption("chess game")
logo = pygame.image.load("image/logo.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((1920, 1080))

background = pygame.image.load("image/echiquier_brun2.jpg")
background = pygame.transform.scale(background, (1080, 1080))
background2 = pygame.image.load("image/echiquier_brun2_inverse.jpg")
background2 = pygame.transform.scale(background2, (1080,1080))

table = pygame.image.load("image/table.jpg")
table = pygame.transform.scale(table, (840, 1080))

bouton_off = pygame.image.load("image/bouton_off.png")
bouton_off = pygame.transform.scale(bouton_off, (150, 150))
bouton_on = pygame.image.load("image/bouton_on.png")
bouton_on = pygame.transform.scale(bouton_on, (150, 150))

led_verte = pygame.image.load("image/led_verte.png")
led_verte = pygame.transform.scale(led_verte, (100, 100))
led_rouge = pygame.image.load("image/led_rouge.png")
led_rouge = pygame.transform.scale(led_rouge, (100, 100))

son_pose = pygame.mixer.Sound("son/pose.wav")


init()

Compteur_tour = -1

ligne = -1
colonne = -1
ligne2 = -1
colonne2 = -1

excolonne2 = 1

alerte = False
annonce = False
exdepart = Roi_Blanc1
exPiece_mange = 0

expieces = {
    "nom": "expieces",
    "type": "expieces",
    "p_gagne": 0,
    "p_total": 0
}

Texte = ""
Annoncement = ""
Annoncement_piece = ""
Interne_back = False

Bouton = False
led = False

Interne = False
valid_deplacement = True
changement = False

while Blanc["Etat"] == True and Noir["Etat"] == True:

    liste_annonce = ["joueur NOIR", "joueur BLANC"]
    liste_alerte = ["deplacement impossible,\nvous n avez pas choisi l une de vos piece,\nrejouez ",
                    "ces coordonnees de depart ne\ncorrespondent a aucune piece,\nrejouez",
                    "vous ne pouvez pas vous deplacez\nsur l une de vos piece,\nrejouez",
                    "ce deplacement n est pas possible\navec cette piece,\nrejouez",
                    "ces coordonnees de depart et/ou d arrivees\nsont en dehors du plateau,\nrejouez"]
    liste_annonce_deplacement = [("Votre "+ str(exdepart["nom"].upper())+ " a ete deplacee a la"),
                                 (str(abs(exdepart["ligne"] - 9)) + "eme ligne, de la colonne "+ str(Chiffre[excolonne2]))]
    liste_annonce_mange = [("Vous avez mange un(e) " + expieces["nom"].upper()),
                           ("Vous avez gagne " + str(expieces["p_gagne"])+" point(s),"),
                           ("Vous avez donc "+str(expieces["p_total"])+ " point(s)"+" au total")]

    piecerie = []
    position = []
    position_x = []
    position_y = []
    for i in range(len(pieces)):
        piecerie += [None]
        position += [None]
        position_x += [None]
        position_y += [None]

    for i in range(len(pieces)):
        piecerie[i] = pygame.image.load(pieces[i]["image"])
        #piecerie[i] = pygame.transform.scale(piecerie[i], (90, 90))

    if Compteur_tour % 2 == 0:
        joueur = Noir["type"]
        Annoncement += "0"
        annonce = True
    else:
        joueur = Blanc["type"]
        Annoncement += "1"
        annonce = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("fermeture du jeu")
            Blanc["Etat"], Noir["Etat"] = False, False
            break

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if pos[0] >= 0 and pos[0] < 1090:
                a = 71
                b = 118.125
                c = a + b
                d = 70
                f = 117.5
                e = d + f
                for i in range(1, 9):
                    if pos[0] >= a and pos[0] < c:
                        if colonne != -1:
                            colonne2 = i
                        else:
                            colonne = i
                    if pos[1] >= d and pos[1] < e:
                        if ligne != -1:
                                ligne2 = i
                        else:
                            ligne = i
                    a = c
                    c = a + b
                    d = e
                    e = d + f

            else:
                if pos[0] >= 1250 and pos[0] <= 1450 and pos[1] <= 200 and pos[1] >= 80:
                    Bouton = not Bouton
                    changement = True
                    if Bouton == True and joueur == Blanc["type"]:
                        Interne_back = True
                        Interne = True
                    else:
                        Interne_back = False
                        Interne = False

    if Blanc["Etat"] == False and Noir["Etat"] == False:
        break


    if ligne != -1 and colonne != -1:
        led = True
    else:
        led = False

    if Bouton == False:
        if Interne_back == True:
            pass
        else:
            screen.blit(background, (0, 0))
            screen.blit(table, (1080, 0))

        screen.blit(bouton_off, (1270, 80))
        if led == True:
            screen.blit(led_verte, (1130, 100))
        else:
            screen.blit(led_rouge, (1130, 100))

        Interne_back = True

        #if changement == True:

        for i in range(len(pieces)):
            pieces[i]["ligne"] = pieces[i]["exligne"]
            pieces[i]["colonne"] = pieces[i]["excolonne"]
            x = (pieces[i]["colonne"]*118-35)
            y = (pieces[i]["ligne"]*118-40)
            screen.blit(piecerie[i], (x,y))
            position_x[i] = x
            position_y[i] = y
            position[i] = position_x[i], position_y[i]
    else:

        Pions = [-8]
        Pion_mange = [-7, -9]
        Pion_debut = [-16]
        if Compteur_tour%2 == 0:
            if Interne_back == True:
                pass
            else:
                screen.blit(background2, (0, 0))
                screen.blit(table, (1080, 0))

                Interne_back = True

            if valid_deplacement == False:
                for i in range(len(pieces)):
                    x = (pieces[i]["colonne"] * 118 - 35)
                    y = (pieces[i]["ligne"] * 118 - 40)
                    screen.blit(piecerie[i], (x, y))
                    position_x[i] = x
                    position_y[i] = y
                    position[i] = position_x[i], position_y[i]
                    valid_deplacement = True
            elif Interne == True:
                pass
            else:
                for i in range(len(pieces)):
                    pieces[i]["colonne"] = abs(pieces[i]["colonne"] - 9)
                    pieces[i]["ligne"] = abs(pieces[i]["ligne"] - 9)
                    x = (pieces[i]["colonne"] * 118 - 35)
                    y = (pieces[i]["ligne"] * 118 - 40)
                    screen.blit(piecerie[i], (x, y))
                    position_x[i] = x
                    position_y[i] = y
                    position[i] = position_x[i], position_y[i]

        else:
            if Interne_back == True:
                pass
            else:
                screen.blit(background, (0, 0))

                screen.blit(table, (1080, 0))
                Interne_back = True

            if Compteur_tour > -1:
                if valid_deplacement == False:
                    for i in range(len(pieces)):
                        x = (pieces[i]["colonne"] * 118 - 35)
                        y = (pieces[i]["ligne"] * 118 - 40)
                        screen.blit(piecerie[i], (x, y))
                        position_x[i] = x
                        position_y[i] = y
                        position[i] = position_x[i], position_y[i]
                elif Interne == True:
                    pass
                else:
                    for i in range(len(pieces)):
                        pieces[i]["colonne"] = abs(pieces[i]["colonne"] - 9)
                        pieces[i]["ligne"] = abs(pieces[i]["ligne"] - 9)
                        x = (pieces[i]["colonne"] * 118 - 35)
                        y = (pieces[i]["ligne"] * 118 - 40)
                        screen.blit(piecerie[i], (x, y))
                        position_x[i] = x
                        position_y[i] = y
                        position[i] = position_x[i], position_y[i]
            else:
                for i in range(len(pieces)):
                    x = (pieces[i]["colonne"] * 118 - 35)
                    y = (pieces[i]["ligne"] * 118 - 40)
                    screen.blit(piecerie[i], (x, y))
                    position_x[i] = x
                    position_y[i] = y
                    position[i] = position_x[i], position_y[i]

        Interne = True

        screen.blit(bouton_on, (1270, 80))
        if led == True:
            screen.blit(led_verte, (1130, 100))
        else:
            screen.blit(led_rouge, (1130, 100))
    changement = False

    if Texte != "" or Annoncement != "":
        police = pygame.font.Font("typwrng.ttf", 30)
        #texte = police.render(Texte, True, pygame.Color("#000000"))
        #rectTexte = texte.get_rect()
        #rectTexte.center = (1500, 540)
        #screen.blit(texte, rectTexte)
        if alerte == True:
            bulle = pygame.Rect(1140, 600, 1920, 800)
            x, y = bulle.topleft
            for espace in Texte.splitlines():
                x, y = screen.blit(police.render(espace, 1, pygame.Color("#000000")), (x, y)).bottomleft
        if annonce == True:
            case = pygame.Rect(1140, 300, 1920, 350)
            case2 = pygame.Rect(1140, 400, 1920, 500)
            case3 = pygame.Rect(1140, 500, 1920, 600)
            u, n = case2.topleft
            g, h = case.topleft
            o, p = case3.topleft
            if Annoncement != "":
                for i in Annoncement:
                    for espacement in liste_annonce[int(i)].splitlines():
                        g, h = screen.blit(police.render(espacement, 1, pygame.Color("#FF0000")), (g, h)).bottomleft
                Annoncement = ""
            if Annoncement_piece != "":
                for i in Annoncement_piece:
                    if i == str(0):
                        for z in range(len(liste_annonce_deplacement)):
                            u, n = screen.blit(police.render(str(liste_annonce_deplacement[int(z)]), 1, pygame.Color("#FF0000")), (u, n)).bottomleft
                    if i == str(1):
                        for z in range(len(liste_annonce_mange)):
                            o, p = screen.blit(police.render(str(liste_annonce_mange[int(z)]), 1, pygame.Color("#FF0000")), (o, p)).bottomleft

                Annoncement_piece = ""


    alerte = False
    annonce = False
    pygame.display.flip()

    if colonne != -1 and ligne != -1 and colonne2 != -1 and ligne2 != -1:

        #initialisation des coordonnes de deplacement
        depart = deplacement(ligne, colonne)
        deplacement2 = deplacement(ligne2, colonne2)

        valid_deplacement = True
        mange = False
        Fin = False

        Texte = ""
        #est ce que c est sur le plateau ?
        if depart <= 63 and deplacement2 <= 63:
            compteur_pieces = 0
            for i in range(len(pieces)):

                #est ce que tu as choisis une de tes piece ?
                if depart == emplacement(pieces[i]):
                    #non
                    if pieces[i]["type"] != joueur:
                        print(Alert_color + "deplacement impossible, vous n avez pas choisi l une de vos piece " + No_color)
                        Texte = liste_alerte[0]
                        alerte = True
                        valid_deplacement = False
                    #oui
                    else:
                        depart = pieces[i]
                    break

                #sinon est ce que tu as choisis une piece ?
                if compteur_pieces == len(pieces)-1:
                    print(Alert_color + "ces coordonnees de depart ne correspondent a aucune piece, rejouez" + No_color)
                    Texte = liste_alerte[1]
                    alerte = True
                    valid_deplacement = False
                    break
                compteur_pieces += 1

            #est ce que tu as tout bien fais avant ?
            if valid_deplacement != False:

                for i in range(len(pieces)):
                    #est ce que tu arrives sur une autre piece ?
                    if deplacement2 == emplacement(pieces[i]):
                        #c est une des tiennes
                        if pieces[i]["type"] == depart["type"]:
                            valid_deplacement = False
                            print(Alert_color +"vous ne pouvez pas vous deplacez sur l une de vos piece, rejouez"+No_color)
                            Texte = liste_alerte[2]
                            alerte = True
                            break
                        #mange la piece ennemie
                        else:
                            mange = True
                            Piece_mange = i
                            break

                if Bouton  == False:
                    if depart["nom"] == Pion["nom"]:
                        depart["deplacement"] = []
                        #print("4 eme", depart["deplacement"])
                        if mange == True:
                            depart["deplacement"] = Dico_pieces[depart["type"]]["mange"]
                        else:
                            depart["deplacement"] = Dico_pieces[depart["type"]]["normal"]
                    # est ce que c'est un pion qui n'a pas bouge ? si oui, agrandir sa liste de mouvement
                        if depart["depart"] == 0 and mange != True:
                            depart["deplacement"] += Dico_pieces[depart["type"]]["debut"]
                else:
                    if depart["nom"] == Pion["nom"]:
                        if mange == True:
                            depart["deplacement"] = Pion_mange
                        elif mange != True:
                            depart["deplacement"] = Pions
                        if depart["depart"] == 0 and mange != True:
                            depart["deplacement"] += Pion_debut
                # est ce que c'est un pion qui peut manger en diagonale ? si oui, agrandir sa liste de mouvement

                liste_listage = []
                if depart["nom"] == Tour["nom"] or depart["nom"] == Fou["nom"] or depart["nom"] == Reine["nom"]:
                    for i in range(len(Dico_pieces[depart["nom"]]["deplacement"])):
                        listage = True
                        lignage = depart["ligne"]
                        colonage = depart["colonne"]
                        verification = emplacement(depart)
                        j = 0
                        while listage == True:
                            j += 1
                            verification += (Dico_pieces[depart["nom"]]["deplacement"][i])
                            passage = False

                            if depart["nom"] != Tour["nom"] and emplacement_pieces(verification, pieces) == False and verification <= 63 and verification >= 0 and abs(deplacement_ligne(verification)-lignage) == 1 and abs(deplacement_colonne(verification)-colonage) == 1:
                                liste_listage += [Dico_pieces[depart["nom"]]["deplacement"][i] * j]
                                colonage, lignage = deplacement_ligne_colonne(verification)
                                passage = True
                            elif depart["nom"] != Tour["nom"] and verification <= 63 and verification >= 0 and abs(deplacement_ligne(verification)-lignage) == 1 and abs(deplacement_colonne(verification)-colonage) == 1:
                                liste_listage += [Dico_pieces[depart["nom"]]["deplacement"][i] * j]
                                listage = False
                                passage = True

                            if depart["nom"] != Fou["nom"] and verification <= 63 and verification >= 0 and deplacement_ligne(verification)-lignage == 0 and abs(deplacement_colonne(verification)-colonage) == 1:
                                if emplacement_pieces(verification, pieces) == False:
                                    liste_listage += [Dico_pieces[depart["nom"]]["deplacement"][i] * j]
                                    colonage, lignage = deplacement_ligne_colonne(verification)
                                else:
                                    liste_listage += [Dico_pieces[depart["nom"]]["deplacement"][i] * j]
                                    listage = False
                                passage = True

                            elif depart["nom"] != Fou["nom"] and verification <= 63 and verification >= 0 and abs(deplacement_ligne(verification)-lignage) == 1 and deplacement_colonne(verification)-colonage == 0:
                                if emplacement_pieces(verification, pieces) == False:
                                    liste_listage += [Dico_pieces[depart["nom"]]["deplacement"][i] * j]
                                else:
                                    liste_listage += [Dico_pieces[depart["nom"]]["deplacement"][i] * j]
                                    listage = False
                                colonage, lignage = deplacement_ligne_colonne(verification)
                                passage = True

                            if passage != True:
                                listage = False

                else:
                    liste_listage = depart["deplacement"]

                # est ce que ton deplacement est valable ?
                for i in range(len(liste_listage)):
                    #oui
                    if deplacement2 - emplacement(depart) == liste_listage[i]:
                        break
                    #non
                    elif i == len(liste_listage)-1:
                        valid_deplacement = False
                        print(Alert_color +"ce deplacement n est pas possible avec cette piece, rejouez"+No_color)
                        Texte = liste_alerte[3]
                        alerte = True

                #si c'est un pion, supprimer l agrandissement de la liste de mouvement precedente
            if Bouton == False:
                if valid_deplacement != False:
                    if depart["nom"] == Pion["nom"]:
                        if depart["depart"] == 0:
                            depart["depart"] += 1
                            print()
                        if depart["type"] == Blanc["type"]:
                            Blanc["normal"] = [-8]
                        else:
                            Noir["normal"] = [8]
            else:
                if valid_deplacement != False:
                    if depart["nom"] == Pion["nom"]:
                        if depart["depart"] == 0:
                            depart["depart"] += 1
                        depart["deplacement"] = Pions

            #si tout est bon le deplacement est valide
            if valid_deplacement == True:
                son_pose.play()
                print()
                depart["ligne"], depart["colonne"] = ligne2, colonne2

                print("Votre" + depart["couleur"],depart["nom"].upper() + No_color + ". a ete deplacee a la" + depart["couleur"], str(abs(depart["ligne"]-9))+"eme"+No_color+" ligne, de la colonne"+ depart["couleur"], str(Chiffre[colonne2])+No_color)
                annonce = True
                excolonne2 = colonne2
                Annoncement_piece += "0"
                if mange == True:
                    if pieces[Piece_mange]["nom"] == Roi["nom"]:
                        Fin = True
                    if Fin != True:
                        print("En vous deplacant, vous avez mange un(e)" + pieces[Piece_mange]["couleur"],
                            pieces[Piece_mange]["nom"].upper() + No_color)
                        Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["Points"] += Dico_pieces[pieces[Piece_mange]["nom"]]["Points"]
                        print("vous avez gagne", Fore.CYAN + str(Dico_pieces[pieces[Piece_mange]["nom"]]["Points"]) + No_color,
                            "point(s), vous avez donc" + Fore.CYAN,
                            str(Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["Points"]), "point(s)" + No_color,
                            "au total")
                        annonce = True
                        Annoncement_piece += "1"

                    # si le roi est mange
                    if pieces[Piece_mange]["nom"] == Roi["nom"]:
                        # finir la partie et l'annoncer
                        Dico_pieces[pieces[Piece_mange]["type"]]["Etat"] = False

                        print("La partie est finit"+depart["couleur"],str(Dico_pieces[depart["type"]]["type"])+No_color, "a GAGNE en mangeant le roi adverse !!!")
                        print(No_color+str(Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["type"]),"a"+Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["couleur"], str(Dico_pieces[depart["type"]]["Points"]), "point(s)" + No_color)
                        print(No_color + str(Dico_pieces[pieces[Piece_mange]["type"]]["type"]), "a"+Dico_pieces[pieces[Piece_mange]["type"]]["couleur"], str(Dico_pieces[pieces[Piece_mange]["type"]]["dico"]["Points"]), "point(s)" + No_color)
                        print("Bien Joue ")

                if depart["nom"] == "Pion" and (ligne2 == 1 or ligne2 == 8):
                    depart["nom"] = Reine["nom"]
                    depart["deplacement"] = Reine["deplacement"]
                    if depart["type"] == "Noir":
                        depart["image"] = Image["Reine_Noir"]
                    else:
                        depart["image"] = Image["Reine_Blanche"]
                    print("Votre Pion est devenue une Reine")

                Compteur_tour += 1
            #sinon tu rejoues
            else:
                pass
        #ta piece n est meme pas sur le plateau
        else:
            print(Alert_color + "ces coordonnees de depart et/ou d arrivees sont en dehors du plateau, rejouez" + No_color)
            Texte = liste_alerte[4]
            alerte = True
            valid_deplacement = False
        colonne, ligne, colonne2, ligne2 = -1, -1, -1, -1

        Interne_back = False
        Interne = False
        if valid_deplacement == True:
            exdepart = depart
            if mange == True:
                expieces["nom"] = pieces[Piece_mange]["nom"]
                expieces["p_gagne"] = Dico_pieces[pieces[Piece_mange]["nom"]]["Points"]
                expieces["p_total"] = Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["Points"]
                del pieces[Piece_mange]
            if Bouton == False:
                depart["exligne"] = depart["ligne"]
                depart["excolonne"] = depart["colonne"]
            else:
                if joueur == Noir["type"]:
                    depart["exligne"] = abs(depart["ligne"] - 9)
                    depart["excolonne"] = abs(depart["colonne"] - 9)
                else:
                    depart["exligne"] = depart["ligne"]
                    depart["excolonne"] = depart["colonne"]
    else:
        if ligne != -1 and colonne == -1:
            colonne, ligne, colonne2, ligne2 = -1, -1, -1, -1
        elif ligne == -1 and colonne != -1:
            colonne, ligne, colonne2, ligne2 = -1, -1, -1, -1