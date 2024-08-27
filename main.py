import pprint
from gracz import Gracz, SpecjalizacjaKlasa, pakiety


def pokaz_menu():
    for specjal in SpecjalizacjaKlasa:
        print(f"{specjal.value}. {specjal.name}")
    print("Bez wyboru - będzie losowa:")


def wybierz_specjal():
    pokaz_menu()
    wybor = (str(input("Wpisz Literę Specjalizacji: "))).upper()

    # Sprawdzenie, czy wybór jest prawidłowy
    if wybor in SpecjalizacjaKlasa._value2member_map_:
        wybrana_specjalizacja = SpecjalizacjaKlasa(wybor)
        return wybrana_specjalizacja.name
    else:
        return None


# Przykładowe użycie
input_klasa = wybierz_specjal()
input_punkty_na_klase = int(input(f"Podaj wartość punktów na klase (domyslne: 30): "))
input_punkty_na_inne = int(
    input(f"Podaj wartość punktów na pozostałe skille (domyslne: 35):")
)

gracz = Gracz(
    pakiety=pakiety,
    punkty_na_klase=input_punkty_na_klase,
    punkty_na_inne=input_punkty_na_inne,
    klasa_nazwa=input_klasa,
)

gracz_wspolczynniki = gracz.wspolczynniki
priti_gracz_wspolczynniki = pprint.pformat(gracz_wspolczynniki, indent=4, width=1)


# PRINTY DO WYCIAGANIA DANYCH:
print(f"\n***********************************\n")
print(f"GRACZ:")
print(f"- klasa: {gracz.klasa_nazwa} - {gracz.klasa_skrot}")
print(f"- współczynniki: \n{priti_gracz_wspolczynniki}")

print("\n- Statystyki postaci:")
for pakiet in gracz.statystyki_postaci:
    print(f"--- {pakiet.nazwa} ---")
    print("Umiejętności:")
    for umiejetnosc in pakiet.umiejetnosci:
        print(f"{umiejetnosc.nazwa}: poziom {umiejetnosc.poziom}")
    print()  # pusta linia oddzielająca pakiety
print(f"***********************************")
