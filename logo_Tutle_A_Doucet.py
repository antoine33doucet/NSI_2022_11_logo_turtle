import turtle
from math import acos
from math import degrees

POSITION_CERCLE_DEPART_HAUT_X = -270 # définit la position x du premier cercle du haut
POSITION_CERCLE_DEPART_HAUT_Y = -25 # définit la position y du premier cercle du haut
RAYON_CERCLES_HAUT = 22 # définit le rayon des cercles du haut
DISTANCE_ENTRE_CERCLE_HAUT= 22 # définit la distance séparant les cercles du haut
NOMBRE_DE_CERCLE_HAUT_MAXIMUM = 7 # définit le nombre de cercles du haut
ALIGNEMENT_HAUT = "vertical" # définit l'alignement du haut
AUGMENTATION_DISTANCE_ENTRE_LES_CERCLES_HAUT = 5 # augmentation de la distance du haut
R_COULEUR_CERCLE_ORIGNE_HAUT = 0.0 # couleur r (pourcentage de rouge) des cercles du haut
G_COULEUR_CERCLE_ORIGNE_HAUT = 1.0 # couleur g (pourcentage de vert) des cercles du haut
B_COULEUR_CERCLE_ORIGNE_HAUT = 0.0 # couleur b (pourcentage de bleu) des cercles du haut
ECARTEMENT_ENTRE_COLONNE_DE_CERCLE_HAUT = 70 # ecartement entre 2 colonnes du haut

POSITION_CERCLE_DEPART_BAS_X = -50 # définit la position x du premier cercle bas
POSITION_CERCLE_DEPART_BAS_Y = -240 # définit la position y du premier cercle bas
RAYON_CERCLES_BAS = 100 # définit le rayon des cercles bas
DISTANCE_ENTRE_CERCLE_BAS = 100 # définit la distance separant les cercles bas
NOMBRE_DE_CERCLE_BAS_MAXIMUM = 2 # définit le nombre de cercles bas
ALIGNEMENT_BAS = "horizontal" # définit l'alignement bas
AUGMENTATION_DISTANCE_ENTRE_LES_CERCLES_BAS = 0 # augmentation de la distance bas
R_COULEUR_CERCLE_ORIGNE_BAS = 1.0 # couleur r (pourcentage de rouge) des cercles du bas
G_COULEUR_CERCLE_ORIGNE_BAS = 0.5 # couleur g (pourcentage de vert) des cercles du bas
B_COULEUR_CERCLE_ORIGNE_BAS = 0.0 # couleur b (pourcentage de bleu) des cercles du bas

NOM_DU_LOGO = "Antoine" # nom du logo
TAILLE_DU_TEXTE = 36 # taille du logo
POSITION_DEPART_NOM_LOGO_X = -75 # définit la position x du logo
POSITION_DEPART_NOM_LOGO_Y = -175 # définit la position y du logo
COULEUR_PRENOM = '#00FFC5' # couleur du logo

POSITION_DEPART_CARRE_X = -250 # définit la position x du carre
POSITION_DEPART_CARRE_Y = -250 # définit la position y du carre
LONGUEUR_COTE_CARRE = 500 # longueur du cote du carre
COULEUR_DU_CARRE = '#0000FF' # couleur du carre

def parametrage_tortue():
    
    """
    Optimise les règlages de la tortue pour être plus rapide
    Args :
    aucun
    """
    
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()

def tracer_un_cercle(cercle_pos_dep_x,cercle_pos_dep_y,cercle_rayon):
    
    """
    trace un cercle, de départ cercle_pos_dep_x et cercle_pos_dep_y et de rayon cercle_rayon
    Args :
    cercle_pos_dep_x (int) : position du départ du cercle x 
    cercle_pos_dep_y (int): position du départ du cercle y 
    cercle_rayon (int) : rayon du cercle 
    """
    
    turtle.goto(cercle_pos_dep_x,cercle_pos_dep_y)
    turtle.right (turtle.heading())
    turtle.begin_fill()
    turtle.circle(cercle_rayon)
    turtle.end_fill()


def trace_intersection_complete_Cos(cercle_pos_dep_x,cercle_pos_dep_y,
                                    cercle_rayon,distance_entre_les_cercles,
                                    alignement_des_cercles):
    """
    trace l'intersection de 2 cercles qui se coupe soit horizontalement soit verticalement avec comme position
    de départ cercle_pos_dep_x et cercle_pos_dep_y, le rayon des 2 cercles cercle_rayon, la distance entre les deux cercles
    distance_entre_les_cercles et l alignement des cercles(vertical ou horizontal).
    
    Args :
    cercle_pos_dep_x (int) : position du départ du cercle x 
    cercle_pos_dep_y (int) : position du départ du cercle y 
    cercle_rayon (int) : rayon du cercle 
    distance_entre_les_cercles (int) : la distance séparant les deux cercles 
    alignement_des_cercles (str) : alignement soit vertical soit horizontal
    """
    if alignement_des_cercles == "vertical":
        angle_inclinaison = 0
    else:
        angle_inclinaison = -90
    if distance_entre_les_cercles < cercle_rayon*2:
        Angle= degrees(acos(distance_entre_les_cercles / (2*cercle_rayon)))
        
        for i in range (0,2) :
            turtle.right (turtle.heading())
            turtle.circle(cercle_rayon,-Angle+angle_inclinaison+180*i)
            turtle.begin_fill()    
            turtle.circle(cercle_rayon,Angle*2)
            turtle.end_fill()
            if alignement_des_cercles == "vertical":
                turtle.goto(cercle_pos_dep_x,cercle_pos_dep_y-distance_entre_les_cercles)
            else:
                turtle.goto(cercle_pos_dep_x-distance_entre_les_cercles,cercle_pos_dep_y)

def groupement_cercle(cercle_pos_dep_x,cercle_pos_dep_y,
                      cercle_rayon,distance_entre_les_cercles,nombre_de_cercle
                      ,alignement_des_cercles,
                      augmentation_distance_entre_cercle,
                      r_couleur_cercle,g_couleur_cercle,b_couleur_cercle):
    """
    trace  une colonne ou une ligne (alignement_des_cercles) de 1 à nombre_de_cercle cercles à partir de la position cercle_pos_dep_x et cercle_pos_dep_y de rayon cercle_rayon,
    chaque cercle est espacé d'une distance_entre_les_cercles plus augmentation_distance_entre_cercle multiplié par (1 à nombre_de_cercle) cercles
    et sont de couleur r_couleur_cercle , g_couleur_cercle , b_couleur_cercle avec une augmentation de 0.15 si celui-ci est inférieur à 1
    ainsi que les intersections, lorsque qu'elles se croisent, leurs couleurs sont aussi en fonction de r_couleur_cercle, g_couleur_cercle, b_couleur_cercle
    Args :
    cercle_pos_dep_x (int) : position du départ du cercle x 
    cercle_pos_dep_y (int) : position du départ du cercle y 
    cercle_rayon (int) : rayon du cercle 
    distance_entre_les_cercles (int) : la distance initiale séparant les cercles 
    nombre_de_cercle (int) : nombre de cercles composant la série
    alignement_des_cercles (str) : alignement soit vertical soit horizontal
    augmentation_distance_entre_cercle (int) : facteur d augmentation de la distance entre les cercles
    r_couleur_cercle (float) : couleur r (pourcentage de rouge) initial 
    g_couleur_cercle (float) : couleur g (pourcentage de vert) initial 
    b_couleur_cercle (float) : couleur b (pourcentage de bleu) initial 
    """
    r = r_couleur_cercle
    g = g_couleur_cercle
    b = b_couleur_cercle
    turtle.fillcolor(r,g,b)
    tracer_un_cercle(cercle_pos_dep_x ,cercle_pos_dep_y,cercle_rayon)
    cercle_en_cours = 0
    while cercle_en_cours < nombre_de_cercle-1:
        cercle_en_cours = cercle_en_cours+1
        if r < 1.0:
            r = r+0.15
        if r > 1.0:
            r = 1.0
       
        if g < 1.0:
            g = g+0.15
        if g > 1.0:
            g = 1.0
            
        if b < 1.0:
            b = b+0.15
        if b > 1.0:
            b =1.0
        turtle.color(r,g,b)
        
        if alignement_des_cercles == "vertical":
            cercle_pos_dep_y = cercle_pos_dep_y+ distance_entre_les_cercles
        else:
            cercle_pos_dep_x = cercle_pos_dep_x+ distance_entre_les_cercles
            
        tracer_un_cercle(cercle_pos_dep_x ,cercle_pos_dep_y,cercle_rayon)
        turtle.color(r,0.8,b)
        trace_intersection_complete_Cos(cercle_pos_dep_x,cercle_pos_dep_y,cercle_rayon,distance_entre_les_cercles,alignement_des_cercles)
        distance_entre_les_cercles = distance_entre_les_cercles + augmentation_distance_entre_cercle 
    turtle.end_fill()

def genere_logo():
    parametrage_tortue() # paramètre la tortue

    turtle.goto(POSITION_DEPART_CARRE_X,POSITION_DEPART_CARRE_Y) # la tortue se positionne à l’emplacement voulu
    turtle.fillcolor(COULEUR_DU_CARRE) # choisit la couleur de remplissage
    turtle.down() # la tortue se met en mode écriture 
    turtle.begin_fill() # la tortue se met en mode remplissage de zone
    for i in range (0,4): # répéter 4 fois
        turtle.forward (LONGUEUR_COTE_CARRE) # avancer de la longueur voulue
        turtle.left(90) # tourne a gauche de 90°
    turtle.end_fill() # termine le remplissage
    turtle.up() # lève le crayon
    
    groupement_cercle(POSITION_CERCLE_DEPART_BAS_X,
                      POSITION_CERCLE_DEPART_BAS_Y ,
                      RAYON_CERCLES_BAS,DISTANCE_ENTRE_CERCLE_BAS,
                      NOMBRE_DE_CERCLE_BAS_MAXIMUM,ALIGNEMENT_BAS,
                      AUGMENTATION_DISTANCE_ENTRE_LES_CERCLES_BAS,
                      R_COULEUR_CERCLE_ORIGNE_BAS,
                      G_COULEUR_CERCLE_ORIGNE_BAS,
                      B_COULEUR_CERCLE_ORIGNE_BAS) #la tortue génère 2 cercles ainsi que l’intersection entre les deux cercles
    
    turtle.goto(POSITION_DEPART_NOM_LOGO_X,POSITION_DEPART_NOM_LOGO_Y) # la tortue se positionne à l’emplacement voulu
    turtle.color(COULEUR_PRENOM) # choisit la couleur d'ecriture
    turtle.write(NOM_DU_LOGO,font=("Arial" ,TAILLE_DU_TEXTE,'')) # la tortue écrit le texte voulu avec la bonne taille et le bon style
    for i in range (1,8): # répéte 7 fois
        groupement_cercle(POSITION_CERCLE_DEPART_HAUT_X+i*ECARTEMENT_ENTRE_COLONNE_DE_CERCLE_HAUT,
                          POSITION_CERCLE_DEPART_HAUT_Y,
                          RAYON_CERCLES_HAUT,
                          DISTANCE_ENTRE_CERCLE_HAUT,
                          NOMBRE_DE_CERCLE_HAUT_MAXIMUM-i+1,
                          ALIGNEMENT_HAUT,
                          AUGMENTATION_DISTANCE_ENTRE_LES_CERCLES_HAUT,
                          R_COULEUR_CERCLE_ORIGNE_HAUT,
                          G_COULEUR_CERCLE_ORIGNE_HAUT,
                          B_COULEUR_CERCLE_ORIGNE_HAUT) #la tortue génére 1 colonne de cercles qui diminue à chaque boucle et trace l'intersection

if __name__ == "__main__":
    genere_logo()
    turtle.done()