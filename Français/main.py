import jeu
import regles

def afficher_menu():
    print("\nMenu :")
    print("1. Jouer au jeu")
    print("2. Voir les règles")
    print("3. Quitter")

def main():
    while True:
        afficher_menu()
        choix_menu = input("Entrez votre choix (1, 2, 3): ")
        if choix_menu == '1':
            jeu.jouer_jeu()
        elif choix_menu == '2':
            regles.afficher_regles()
        elif choix_menu == '3':
            print("Merci d'avoir joué ! Au revoir.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
