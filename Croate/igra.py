import random

def dobiti_izbor_korisnika():
    izbor = input("Unesite svoj izbor (kamen, papir, makaze): ").lower()
    while izbor not in ["kamen", "papir", "makaze"]:
        print("Neispravan izbor. Molim pokušajte ponovno.")
        izbor = input("Unesite svoj izbor (kamen, papir, makaze): ").lower()
    return izbor

def dobiti_izbor_racunala():
    return random.choice(["kamen", "papir", "makaze"])

def odrediti_pobjednika(izbor_korisnika, izbor_racunala):
    if izbor_korisnika == izbor_racunala:
        return "Izjednačeno"
    elif (izbor_korisnika == "kamen" and izbor_racunala == "makaze") or \
         (izbor_korisnika == "papir" and izbor_racunala == "kamen") or \
         (izbor_korisnika == "makaze" and izbor_racunala == "papir"):
        return "Vi ste pobjedili!"
    else:
        return "Računalo je pobjedilo!"

def igrati_igru():
    izbor_korisnika = dobiti_izbor_korisnika()
    izbor_racunala = dobiti_izbor_racunala()
    print(f"Vi ste odabrali: {izbor_korisnika}")
    print(f"Računalo je odabralo: {izbor_racunala}")
    rezultat = odrediti_pobjednika(izbor_korisnika, izbor_racunala)
    print(rezultat)
