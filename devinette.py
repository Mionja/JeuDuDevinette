def jeux():
    global score
    i = 0
#inmportation du nombre aléatoire
    import random
    n = random.randint(0, 100)
    #print(str(n))
    while i < 10:
#Au cas où l'utilisateur ne saisit pas un nombre
        a = 0
        while a == 0:
            user_number = input("\nDevinnez un nombre entre 0 à 100: ")
            try:
                user_number = int(user_number)
                a = 1
                if user_number < 0 or user_number > 100:
                    print("***Seulement un nombre entre 0 et 100")
                    a = 0
            except:
                print("XXXXXXX----Veuillez saisir un nombre----XXXXXX")
#Continuer avec les instructions si l'utilisateur saisit bien un nombre
        if user_number == n:
            print("Vous avez trouvé")
            break
        elif user_number < n :
            print("Augmentez encore plus\t Il vous reste ", str(9-i), "essai" )
            i += 1
        elif user_number > n :
            print("Diminuez un peu plus \t Il vous reste", str(9-i), "essai")
            i += 1
        if i == 10:
            print("vous avez perdu\t C'était ", n)
            break
    score = 9 - i
    if score < 0:
        score = 0


def reesayer():
    try_again = str(input("Entrez Q pour quitter ou appuyer sur n'importe quoi apart le boutton power off pour recommencer:\t"))
    if try_again == "Q" or try_again == "q":
        print("\n\n\t\t\t\t---Merci d'avoir jouer au jeux---")
    else:
        start()


def start():
#premier utilisateur
    user1 = input("Entrez le nom du premier utilisateur: ")
    print("Salut", user1)
    jeux()
    score1 = score
    print("Le score de ", str(user1), "est", score1, "/10\n")
#deuxieme utilisateur
    user2 = input("Entrez le nom du deuxième utilisateur: ")
    print("Salut", user2)
    jeux()
    score2 = score
    print("Le score de ", str(user2), "est", score2, "/10\n")

#resultat du match
    if score1 < score2:
        print("\t", "§ Félicitation! ", "\t", user2, "a gagné §\n")
    elif score2 < score1:
        print("\t", "§ Félicitation! ", "\t", user1, "a gagné §\n")
    else:
       print("\t-Egalité-", "\n")
    reesayer()


def salut(user_name):
    print("Salut", user_name)


""""---------------------------- COMMENCEMENT DU JEUX----------------------------"""
bienvenu = "Bienvenu dans le jeux du devinnette"
print("\n", bienvenu.center(100, '-'), "\n")
start()
