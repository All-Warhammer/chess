from colorama import*
global Piece_mange
from test_echiquier_pieces import*
import pygame

pygame.init()

pygame.display.set_caption("chess game")
logo = pygame.image.load("image/logo.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((1920, 1080))

background = pygame.image.load("image/echiquier_brun2.jpg")
background = pygame.transform.scale(background, (1080,1080))

background2 = pygame.image.load("image/echiquier_brun2_inverse.jpg")
background2 = pygame.transform.scale(background2, (1080,1080))

table = pygame.image.load("image/table.jpg")
table = pygame.transform.scale(table, (840,1080))

init()

Compteur_tour = -1

ligne = -1
colonne = -1
ligne2 = -1
colonne2 = -1

liste_alerte = ["deplacement impossible,\nvous n avez pas choisi l une de vos piece,\nrejouez ","ces coordonnees de depart ne correspondent\na aucune piece,\nrejouez","vous ne pouvez pas vous deplacez\nsur l une de vos piece,\nrejouez", "ce deplacement n est pas possible\navec cette piece,\nrejouez","ces coordonnees de depart et/ou d arrivees\nsont en dehors du plateau,\nrejouez"]

Texte = ""

Interne = False

Interne_back = False

valid_deplacement = False

while Blanc["Etat"] == True and Noir["Etat"] == True:

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
        piecerie[i] = pygame.transform.scale(piecerie[i], (90, 90))

    if Texte != "":
        police = pygame.font.Font("typwrng.ttf", 30)
        #texte = police.render(Texte, True, pygame.Color("#000000"))
        #rectTexte = texte.get_rect()
        #rectTexte.center = (1500, 540)
        #screen.blit(texte, rectTexte)
        bulle = pygame.Rect(1100, 500, 1920, 700)
        x, y = bulle.topleft
        for espace in Texte.splitlines():
            x, y = screen.blit(police.render(espace, 1, pygame.Color("#000000")), (x, y)).bottomleft

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
        elif Interne == False:
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

        Interne = False

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

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("fermeture du jeu")
            Blanc["Etat"], Noir["Etat"] = False, False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

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

    if colonne != -1 and ligne != -1 and colonne2 != -1 and ligne2 != -1:

        if Compteur_tour%2 == 0:
            joueur = Noir["type"]
            print()
            print()
            print(Noir["couleur"] + "joueur NOIR" + No_color)
        else:
            joueur = Blanc["type"]
            print()
            print()
            print(Blanc["couleur"] + "joueur BLANC" + No_color)

        #initialisation des coordonnes de deplacement
        depart = deplacement(ligne, colonne)
        deplacement2 = deplacement(ligne2, colonne2)

        mange = False
        Fin = False
        valid_deplacement = True

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
                        valid_deplacement = False
                    #oui
                    else:
                        depart = pieces[i]
                    break

                #sinon est ce que tu as choisis une piece ?
                if compteur_pieces == len(pieces)-1:
                    print(Alert_color + "ces coordonnees de depart ne correspondent a aucune piece, rejouez" + No_color)
                    Texte = liste_alerte[1]
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
                            break
                        #mange la piece ennemie
                        else:
                            mange = True
                            Piece_mange = i
                            break

                # est ce que c'est un pion qui peut manger en diagonale ? si oui, agrandir sa liste de mouvement
                if mange == True and depart["nom"] == Pion["nom"]:
                    depart["deplacement"] = Dico_pieces[depart["type"]]["mange"]
                # est ce que c'est un pion qui n'a pas bouge ? si oui, agrandir sa liste de mouvement
                if depart["nom"] == "Pion" and depart["depart"] == 0:
                    depart["deplacement"] += Dico_pieces[depart["type"]]["debut"]

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

                #si c'est un pion, supprimer l agrandissement de la liste de mouvement precedente
                if depart["nom"] == Pion["nom"] and valid_deplacement != False:
                    if depart["depart"] == 0:
                        depart["depart"] += 1
                    depart["deplacement"] = Dico_pieces[depart["type"]]["normal"]

            #si tout est bon le deplacement est valide
            if valid_deplacement == True:
                print()
                depart["ligne"], depart["colonne"] = ligne2, colonne2

                print("Votre" + depart["couleur"],depart["nom"].upper() + No_color + ". a ete deplacee a la" + depart["couleur"], str(abs(depart["ligne"]-9))+"eme"+No_color+" ligne, de la colonne"+ depart["couleur"], str(Chiffre[colonne2])+No_color)

                if mange == True:
                    if pieces[Piece_mange]["nom"] == Roi["nom"]:
                        Fin = True
                    if Fin != True:
                        print("En vous deplacant, vous avez mange un(e)" + pieces[Piece_mange]["couleur"],
                            pieces[Piece_mange]["nom"].upper() + No_color)
                        Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["Points"] += Dico_pieces[pieces[Piece_mange]["nom"]]["Points"]
                        print("Dico",Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["Points"])
                        print("vous avez gagne", Fore.CYAN + str(Dico_pieces[pieces[Piece_mange]["nom"]]["Points"]) + No_color,
                            "point(s), vous avez donc" + Fore.CYAN,
                            str(Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["Points"]), "point(s)" + No_color,
                            "au total")

                    # si le roi est mange
                    if pieces[Piece_mange]["nom"] == Roi["nom"]:
                        # finir la partie et l'annoncer
                        Dico_pieces[pieces[Piece_mange]["type"]]["Etat"] = False

                        print("La partie est finit"+depart["couleur"],str(Dico_pieces[depart["type"]]["type"])+No_color, "a GAGNE en mangeant le roi adverse !!!")
                        print(No_color+str(Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["type"]),"a"+Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["couleur"], str(Dico_pieces[pieces[Piece_mange]["type"]]["Inverse"]["Points"]), "point(s)" + No_color)
                        print(No_color + str(Dico_pieces[pieces[Piece_mange]["type"]]["type"]), "a"+Dico_pieces[pieces[Piece_mange]["type"]]["couleur"], str(Dico_pieces[pieces[Piece_mange]["type"]]["Points"]), "point(s)" + No_color)
                        print("Bien Joue ")

                    del pieces[Piece_mange]

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
            valid_deplacement = False

        colonne, ligne, colonne2, ligne2 =-1, -1, -1, -1

        Interne_back = False

    else:
        if ligne != -1 and colonne == -1:
            colonne, ligne, colonne2, ligne2 = -1, -1, -1, -1
        elif ligne == -1 and colonne != -1:
            colonne, ligne, colonne2, ligne2 = -1, -1, -1, -1