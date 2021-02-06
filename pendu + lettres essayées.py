# Créé par Quentin, le 04/02/2021 en Python 3.7

solution ="python"
tours =9

affichage = "_ _ _ _ _ _"
lettres_trouvees =""
lettres_essayees =""

while tours > 0:
    print("lance toi !")

    print(affichage)
    print(lettres_essayees)
    proposition = input("").lower()

    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("continue")
    else:
        tours= tours-1
        print(tours)
        lettres_trouvees = lettres_trouvees
        lettres_essayees = lettres_essayees + proposition
    affichage=""

    for lettres in solution:
        if lettres in lettres_trouvees:
            affichage = affichage + lettres
        else:
            affichage = affichage + "_"
    if "_" not in affichage:
        print("Bien joué !!!!")














