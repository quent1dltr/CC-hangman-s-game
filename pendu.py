# Créé par Quentin, le 04/02/2021 en Python 3.7

solution ="python"
tours =9

affichage = "_ _ _ _ _ _"
lettres_trouvees ="6"

while tours > 0:
    print("lance toi !")

    print(affichage)
    proposition = input("").lower()

    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("continue")
    else:
        tours= tours-1
        print(tours)
    affichage=""

    for lettres in solution:
        if lettres in lettres_trouvees:
            affichage = affichage + lettres
        else:
            affichage = affichage + "_"
    if "_" not in affichage:
        print("Bien joué !!!!")











