print("Hello LAJ's world")  # nous ne somme pas obligé d'utilise ";" comme marque de fin d'instruction, le retour a la ligne c'est la plus utilisé

score = int()  # tout type est une classe ( numbers:-entiers et reels- // strings:-chaines
# print(type(score))
total = 5  # une autre maniere de declaration ( affectation )

response = input("Êtes-vous prêt pour commencer a jouer ? (oui/non): \n")   # "\n" c'est pour faire un saut à la ligne
if response.lower() == "oui":                                      # faites attenton a l'indentation
    # 1 ----------------------------------------------------------------------------------------------------------------
    response = input("1. Quel est votre language de programmation preferé ? \n")      # "=" c'est l'affection
    if response.lower() == "python":                               # "==" c'est l'egalité
        score = score + 1
        print("C'est tres bien \n")
    else:
        print("FAUT, ca doit être PYTHON. je m'en fous -_- \n")

    # 2 ----------------------------------------------------------------------------------------------------------------
    repense = input("2. Quelle est votre niveau en algorithmique selon votre propre jugement ? (en %) \n")
    rep = int(response)  # conversion de str vers int // car le input est toujours une chaine de caractères
    if rep >= 50:
        score = score + 1
        print("Bien, on peut attaquer Python. \n qui est un language multi-paradigme et multi-plateforme ")
    else:
        print("On va attaquer Python quand même, mais essayez de développer vos notions d'algo \n")

    # 3 ----------------------------------------------------------------------------------------------------------------
    response = input("3. Python est-il un language compilé ou bien interprété? \n")
    if response.lower() == "interprete":
        score = score + 1
        print("Parfait, mais est-ce que vous l'avez réellement compris, ou c'est juste un coup de chance? expliquant le alors quand même :D \n")
    else:
        print("Bah non!, mais ce n'est pas grave c'est l'occasion de l'expliquer \n")

    # 4 ----------------------------------------------------------------------------------------------------------------
    response = input("4. Python est-il sensible à la casse ? \n")
    if response.lower() == "oui":
        score = score + 1
        print("Parfait, car il fait la différence entre la majuscule et la minuscule \n")
    else:
        print("Python fait la différence entre la majuscule et la minuscule \n")

    # 5 ----------------------------------------------------------------------------------------------------------------
    response = input("5. Python a-t-il le même typage que java(statique) ou bien il a un typage dynamique ?? \n")
    if response.lower() == "dynamique":
        score = score + 1
        print("Magnifique, Python est 'fortement typé' car il arrive a détecter directement le type de nos variables lors de l'initialisation \n")
    else:
        print("Python procède un typage dynamique donc on dit qu'il est 'fortement typé' car il arrive à détecter directement le type de nos variables lors de l'initialisation \n")


    print("Merci de faire confiance en Learn and joy, vous avez eu", score, "questions correctes \n")  # nous n'avions pas fait de conversion ici car on a utilisé là "," et non pas la concatenation"+"
    note = (score/total) * 100

    print("Vous avez la note de: ", str(note) + "% \n") # On peut faire la concatenation avec le "+"
                                                        # On ne peut pas afficher deux types différents au sein de la fonction print() du moment ou on utilise la concatenation (avec le "+") 
                                                        # si on utilise la "," a la place du "+" on peut éviter d'utiliser la conversion (autrement dit le casting)
else:
    print("Essayez ulterieurement \n")

print("Merci, au revoir")
