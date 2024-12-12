import igra
import pravila

def prikazati_meni():
    print("\nMeni:")
    print("1. Igrati igru")
    print("2. Pogledati pravila")
    print("3. Izlaz")

def main():
    while True:
        prikazati_meni()
        izbor_menija = input("Unesite svoj izbor (1, 2, 3): ")
        if izbor_menija == '1':
            igra.igrati_igru()
        elif izbor_menija == '2':
            pravila.prikazati_pravila()
        elif izbor_menija == '3':
            print("Hvala vam što ste igrali! Doviđenja.")
            break
        else:
            print("Neispravan izbor. Molim pokušajte ponovno.")

if __name__ == "__main__":
    main()
