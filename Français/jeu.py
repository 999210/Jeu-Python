import random

def obtenir_choix_utilisateur():
    choix = input("Entrez votre choix (pierre, papier, ciseaux): ").lower()
    while choix not in ["pierre", "papier", "ciseaux"]:
        print("Choix invalide. Veuillez réessayer.")
        choix = input("Entrez votre choix (pierre, papier, ciseaux): ").lower()
    return choix

def obtenir_choix_ordinateur():
    return random.choice(["pierre", "papier", "ciseaux"])

def determiner_gagnant(choix_utilisateur, choix_ordinateur):
    if choix_utilisateur == choix_ordinateur:
        return "Égalité"
    elif (choix_utilisateur == "pierre" and choix_ordinateur == "ciseaux") or \
         (choix_utilisateur == "papier" and choix_ordinateur == "pierre") or \
         (choix_utilisateur == "ciseaux" and choix_ordinateur == "papier"):
        return "Vous avez gagné !"
    else:
        return "L'ordinateur a gagné !"

def jouer_jeu():
    choix_utilisateur = obtenir_choix_utilisateur()
    choix_ordinateur = obtenir_choix_ordinateur()
    print(f"Vous avez choisi: {choix_utilisateur}")
    print(f"L'ordinateur a choisi: {choix_ordinateur}")
    resultat = determiner_gagnant(choix_utilisateur, choix_ordinateur)
    print(resultat)
