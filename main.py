import pprint
from gracz import Gracz, SpecjalizacjaKlasa, pakiety


def pobierz_wartosc(tekst: str, domyslne: int):
    try:
        input_value = input(tekst)
        if input_value.strip() == "":
            return domyslne  # Domyślna wartość
        return int(input_value)
    except ValueError:
        print(f"Niepoprawna wartość, ustawiam domyślną: {domyslne}")
        return domyslne


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


input_punkty_na_klase = pobierz_wartosc(
    tekst="Podaj wartość punktów na klase (domyslne: 30): ", domyslne=30
)

input_punkty_na_inne = pobierz_wartosc(
    tekst=f"Podaj wartość punktów na pozostałe skille (domyslne: 35):", domyslne=35
)


gracz = Gracz(
    pakiety=pakiety,
    punkty_na_klase=input_punkty_na_klase,
    punkty_na_inne=input_punkty_na_inne,
    klasa_nazwa=input_klasa,
)

gracz_wspolczynniki = gracz.wspolczynniki
kolejnosc_wspolczynnikow = ["Zręczność", "Percepcja", "Charakter", "Spryt", "Budowa"]

posortowany_slownik = {
    key: gracz_wspolczynniki[key] for key in kolejnosc_wspolczynnikow
}

priti_gracz_wspolczynniki = pprint.pformat(
    posortowany_slownik, indent=4, width=1, sort_dicts=False
)

# PRINTY DO WYCIAGANIA DANYCH:
print(f"\n***********************************\n")
print(f"GRACZ:")
print(f"- klasa: {gracz.klasa_nazwa} - {gracz.klasa_skrot}")
print(f"- współczynniki: \n{priti_gracz_wspolczynniki}")


# Przygotowanie danych statystyk aby wypisane były główne staty w kolejności
gracz_statystyki = gracz.statystyki_postaci

kolejnosc_statystyki = [
    "Walka wręcz",
    "Broń strzelecka",
    "Broń dystansowa",
    "Prowadzenie pojazdów",
    "Zdolności manualne",
    "Orientacja w terenie",
    "Spostrzegawczość",
    "Kamuflaż",
    "Przetrwanie",
    "Negocjacje",
    "Empatia",
    "Siła woli",
    "Medycyna",
    "Technika",
    "Sprzęt",
    "Pirotechnika",
    "Sprawność",
    "Jeździectwo",
]

# Tworzymy słownik, który przypisuje numer kolejności do każdej nazwy umiejętności
kolejnosc_map = {nazwa: index for index, nazwa in enumerate(kolejnosc_statystyki)}

posortowana_lista = sorted(
    gracz_statystyki,
    key=lambda pakiet: kolejnosc_map.get(pakiet.nazwa, len(kolejnosc_statystyki)),
)


print("\n- Statystyki postaci:")
for pakiet in posortowana_lista:
    print(f"--- {pakiet.nazwa} ---")
    print("Umiejętności:")
    for umiejetnosc in pakiet.umiejetnosci:
        print(f"{umiejetnosc.nazwa}: poziom {umiejetnosc.poziom}")
    print()  # pusta linia oddzielająca pakiety
print(f"***********************************")
