import game
import rules

def display_menu():
    print("\nMenu:")
    print("1. Play the game")
    print("2. View the rules")
    print("3. Quit")

def main():
    while True:
        display_menu()
        menu_choice = input("Enter your choice (1, 2, 3): ")
        if menu_choice == '1':
            game.play_game()
        elif menu_choice == '2':
            rules.display_rules()
        elif menu_choice == '3':
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
