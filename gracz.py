# Generator do tworzenia NPCów i nie tylko w neuroshimie

import math
import random
from enum import Enum


# Definicja enum dla Specjalizacji
class SpecjalizacjaKlasa(Enum):
    TECHNIK = "T"
    WOJOWNIK = "W"
    RANGER = "R"
    CWANIAK = "C"


class Umiejetnosc:
    def __init__(self, nazwa, poziom: int = 0, klasa=[]):
        self.nazwa = nazwa
        self.poziom = poziom
        self.klasa = klasa

    def podnies_umiejetnosc(self):
        self.poziom += 1


class Pakiet:
    def __init__(
        self,
        nazwa,
        klasa: str,
        umiejetnosci: Umiejetnosc = [],
    ):
        self.nazwa = nazwa
        self.klasa = klasa
        self.umiejetnosci = umiejetnosci

    def __str__(self) -> str:
        return f"Pakiet: {self.nazwa} - klasa: {self.klasa}"

    def kup_pakiet(self):
        for umiejetnosc in self.umiejetnosci:
            umiejetnosc.podnies_umiejetnosc()
        return self


# Specjalizacje i Pakiety:
pakiety = [
    # "Walka wręcz",
    Pakiet(
        "Walka wręcz",
        ["W"],
        [
            Umiejetnosc("bijatyka", klasa=["W"]),
            Umiejetnosc("broń ręczna", klasa=["W"]),
            Umiejetnosc("rzucanie", klasa=["W"]),
        ],
    ),
    # "Broń strzelecka"
    Pakiet(
        "Broń strzelecka",
        ["W"],
        [
            Umiejetnosc("Pistolety", klasa=["W"]),
            Umiejetnosc("Karabiny", klasa=["W"]),
            Umiejetnosc("Broń maszynowa", klasa=["W"]),
        ],
    ),
    # "Broń dystansowa"
    Pakiet(
        "Broń dystansowa",
        ["W", "R"],
        [
            Umiejetnosc("Łuk", klasa=["W", "R"]),
            Umiejetnosc("Kusza", klasa=["W", "R"]),
            Umiejetnosc("Proca", klasa=["W", "R"]),
        ],
    ),
    # "Prowadzenie pojazdów"
    Pakiet(
        "Prowadzenie pojazdów",
        ["T"],
        [
            Umiejetnosc("Samochód", klasa=["T"]),
            Umiejetnosc("Ciężarówka", klasa=["T"]),
            Umiejetnosc("Motocykl", klasa=["T"]),
        ],
    ),
    # "Zdolności manualne"
    Pakiet(
        "Zdolności manualne",
        ["C"],
        [
            Umiejetnosc("Kradzież kieszonkowa", klasa=["C"]),
            Umiejetnosc("Zwinne dłonie", klasa=["C"]),
            Umiejetnosc("Otwieranie zamków", klasa=["C"]),
        ],
    ),
    # Orientacja w terenie
    Pakiet(
        "Orientacja w terenie",
        ["R"],
        [
            Umiejetnosc("Wyczucie kierunku", klasa=["R"]),
            Umiejetnosc("Tropienie", klasa=["R"]),
            Umiejetnosc("Przygotowanie pułapki", klasa=["R"]),
        ],
    ),
    # Spostrzegawczość
    Pakiet(
        "Spostrzegawczość",
        ["R"],
        [
            Umiejetnosc("Nasłuchiwanie", klasa=["R"]),
            Umiejetnosc("Wypatrywanie", klasa=["R"]),
            Umiejetnosc("Czujność", klasa=["R"]),
        ],
    ),
    # Kamuflaż
    Pakiet(
        "Kamuflaż",
        ["C", "R"],
        [
            Umiejetnosc("Skradanie się", klasa=["C", "R"]),
            Umiejetnosc("Ukrywanie się", klasa=["C", "R"]),
            Umiejetnosc("Maskowanie", klasa=["C", "R"]),
        ],
    ),
    # Przetrwanie
    Pakiet(
        "Przetrwanie",
        ["R"],
        [
            Umiejetnosc("Łowiectwo", klasa=["R"]),
            Umiejetnosc("Zdobywanie wody", klasa=["R"]),
            Umiejetnosc("Znajomość terenu", klasa=["R"]),
        ],
    ),
    # Negocjacje
    Pakiet(
        "Negocjacje",
        ["C"],
        [
            Umiejetnosc("Persfazja", klasa=["C"]),
            Umiejetnosc("Zastraszanie", klasa=["C"]),
            Umiejetnosc("Zdolności przywódcze", klasa=["C"]),
        ],
    ),
    # Empatia
    Pakiet(
        "Empatia",
        ["C"],
        [
            Umiejetnosc("Postrzeganie emocji", klasa=["C"]),
            Umiejetnosc("Blef", klasa=["C"]),
            Umiejetnosc("Opieka nad zwierzętami", klasa=["C"]),
        ],
    ),
    # Siła woli
    Pakiet(
        "Siła woli",
        ["W"],
        [
            Umiejetnosc("Odporność na ból", klasa=["W"]),
            Umiejetnosc("Niezłomność", klasa=["W"]),
            Umiejetnosc("Morale", klasa=["W"]),
        ],
    ),
    # Medycyna
    Pakiet(
        "Medycyna",
        ["R", "T"],
        [
            Umiejetnosc("Leczenie ran", klasa=["R", "T"]),
            Umiejetnosc("Leczenie chorób", klasa=["R", "T"]),
            Umiejetnosc("Pierwsza pomoc", klasa=["R", "T"]),
        ],
    ),
    # Technika
    Pakiet(
        "Technika",
        ["T"],
        [
            Umiejetnosc("Mechanika", klasa=["T"]),
            Umiejetnosc("Elektronika", klasa=["T"]),
            Umiejetnosc("Komputery", klasa=["T"]),
        ],
    ),
    # Sprzęt
    Pakiet(
        "Sprzęt",
        ["T"],
        [
            Umiejetnosc("Maszyny ciężkie", klasa=["T"]),
            Umiejetnosc("Wozy bojowe", klasa=["T"]),
            Umiejetnosc("Kutry", klasa=["T"]),
        ],
    ),
    # Pirotechnika
    Pakiet(
        "Pirotechnika",
        ["T", "W"],
        [
            Umiejetnosc("Rusznikarstwo", klasa=["T", "W"]),
            Umiejetnosc("Wyrzutnie", klasa=["T", "W"]),
            Umiejetnosc("Materiały wubuchowe", klasa=["T", "W"]),
        ],
    ),
    # Sprawność
    Pakiet(
        "Sprawność",
        ["R"],
        [
            Umiejetnosc("Pływanie", klasa=["R"]),
            Umiejetnosc("Wspinaczka", klasa=["R"]),
            Umiejetnosc("Kondycja", klasa=["R"]),
        ],
    ),
    # Jeździectwo
    Pakiet(
        "Jeździectwo",
        ["R"],
        [
            Umiejetnosc("Jazda konna", klasa=["R"]),
            Umiejetnosc("Powożenie", klasa=["R"]),
            Umiejetnosc("Ujeżdżanie", klasa=["R"]),
        ],
    ),
]


class Gracz:
    pakiety_do_wykupienia = 18
    pakiety_do_wykupienia_per_klasa = 5

    def __init__(
        self,
        pakiety: list,
        punkty_na_klase: int = 30,
        punkty_na_inne: int = 35,
        klasa_nazwa: str = None,
    ) -> None:
        self.pakiety = pakiety
        self.punkty_na_klase = punkty_na_klase
        self.punkty_na_inne = punkty_na_inne
        self.wspolczynniki = self._generuj_wspolczynniki()

        self.klasa_nazwa, self.klasa_skrot = self._wybierz_klase(
            klasa_nazwa if klasa_nazwa else None
        )

        self.statystyki_postaci = self.statystyki()

    # Generowanie losowych współczynników
    def _generuj_wspolczynniki(self):
        wspolczynniki = {
            "Zręczność": 0,
            "Percepcja": 0,
            "Charakter": 0,
            "Spryt": 0,
            "Budowa": 0,
        }

        # Generowanie listy umiejętności
        skill_lista = []

        for _ in range(
            len(wspolczynniki) + 1
        ):  # 5 współczynników + 1 dodatkowa wartość
            skill_points = [random.randint(1, 20) for _ in range(3)]
            skill_temp_value = sum(skill_points) / 3
            liczba_do_zapisania = math.ceil(skill_temp_value)
            skill_lista.append(liczba_do_zapisania)

        # Usuwanie najmniejszej wartości
        skill_lista.remove(min(skill_lista))

        # Przypisywanie losowych wartości do współczynników
        random.shuffle(skill_lista)
        for i, key in enumerate(wspolczynniki):
            wspolczynniki[key] = skill_lista[i]

        return wspolczynniki

    # Wybieranie losowej specjalizacji
    def _wybierz_klase(self, klasa_nazwa: str = None):
        if not klasa_nazwa:
            losowa_klasa = random.choice(list(SpecjalizacjaKlasa))
            print(f"Wylosowano klase: {losowa_klasa.name} - {losowa_klasa.value}")
        else:
            losowa_klasa = SpecjalizacjaKlasa[klasa_nazwa]
            print(f"Wybrałeś klase: {losowa_klasa.name}")
        return losowa_klasa.name, losowa_klasa.value

    def _liczba_pakietow_do_wykupienia(self, liczba_pakietow_dostepnych: int):
        result = random.randint(0, liczba_pakietow_dostepnych)
        print(f"Liczba pełnych pakietów do wykupienia: {result}")
        return result

    def _maksymalna_liczba_pakietow(self, liczba_punktow: int):
        # wyliczenie maksymalnej dostępnej liczby pakietów do wykupienia według dostarczonych punktów na inne skille:
        max_pakiety = math.floor(liczba_punktow / 5)

        # Losowa liczba pakietów do wykupienia z punktów innych skili:
        pakiety_do_kupienia = self._liczba_pakietow_do_wykupienia(max_pakiety)
        print(
            f"Z dostępnej liczby punktów maksymalnie można kupić {pakiety_do_kupienia} pełnych pakietów."
        )
        return pakiety_do_kupienia

    def _sprawdz_pakiety(self, punkty, klasa: bool = True):
        kupiono = 0

        # Losowa liczba pakietów do wykupienia z punktów innych skili:
        pakiety_do_kupienia = self._maksymalna_liczba_pakietow(punkty)
        target_punkty = "punkty_na_klase" if klasa else "punkty_na_inne"

        print(f"Pakiety do kupienia: {pakiety_do_kupienia} - czy na klase: {klasa}")
        for _ in range(0, pakiety_do_kupienia):
            if kupiono < pakiety_do_kupienia:
                # Utworzenie losowej listy pakietów za każdym obrotem pętli:
                random.shuffle(pakiety)

                # Sprawdzenie umiejętności w każdym pakiecie
                for pakiet in pakiety:
                    if not klasa or self.klasa_skrot in pakiet.klasa:
                        if all(
                            umiejetnosc.poziom == 0
                            for umiejetnosc in pakiet.umiejetnosci
                        ):
                            print(f"KUPIĆ - {pakiet.nazwa}")
                            kupiono += 1
                            pakiet.kup_pakiet()
                            setattr(
                                self, target_punkty, getattr(self, target_punkty) - 5
                            )
                            continue
            else:
                break
        print(f"Koniec kupowania pakietów dla {'klasy' if klasa else 'innych'}")
        return self.pakiety

    def _sprawdz_pakiety_klasa(self):
        kupiono = 0

        # przefiltorwana pakietów lista według klasy:
        filtered_list = [item for item in pakiety if self.klasa_skrot in item.klasa]

        # Losowa liczba pakietów do wykupienia z punktów innych skili:
        pakiety_do_kupienia = self._maksymalna_liczba_pakietow(self.punkty_na_klase)

        print(
            f"pakiety do kupienia na klase: {pakiety_do_kupienia} z {len(filtered_list)} możliwych"
        )

        while kupiono < pakiety_do_kupienia and kupiono < len(filtered_list):
            wynik = random.choice(filtered_list)

            # Sprawdzenie umiejętności w każdym pakiecie
            for umiejetnosc in wynik.umiejetnosci:
                # Już kupiona umiejętność w pakiecie - przeskakujemy dalej
                if umiejetnosc.poziom != 0:
                    print(f"Pakiet już kupiony: {wynik.nazwa}")
                    break
            else:
                print(f"KUPIĆ - {wynik.nazwa}")
                kupiono += 1
                wynik.kup_pakiet()
                self.punkty_na_klase -= 5
                continue
        print(f"Koniec kupowania pakietów dla klasy")
        return pakiety

    def _kupuj_staty_klasa(self, staty):
        print(f"punkty_na_klase: {self.punkty_na_klase}")
        # Utworzenie losowej listy pakietów za każdym obrotem pętli:
        filtered_list = [item for item in pakiety if self.klasa_skrot in item.klasa]

        while self.punkty_na_klase > 0:
            # Losowanie pakietu:
            wynik = random.choice(filtered_list)
            print(f"Wylosowany pakiet klasy: {wynik.nazwa}")

            # Losowanie skilla:
            podnoszony_skill = random.choice(wynik.umiejetnosci)

            # Już kupiona umiejętność w pakiecie - przeskakujemy dalej
            if podnoszony_skill.poziom == 0 and self.punkty_na_klase >= 3:
                podnoszony_skill.podnies_umiejetnosc()
                self.punkty_na_klase -= 3
                print(
                    f"\tPodnoszony poziom: {podnoszony_skill.nazwa} na 1 - pozostało: {self.punkty_na_klase} punktów."
                )
                continue

            elif podnoszony_skill.poziom > 0 and self.punkty_na_klase >= 2:
                nowy_poziom_skila = podnoszony_skill.poziom + 1
                if self.punkty_na_klase - nowy_poziom_skila >= 0:
                    podnoszony_skill.podnies_umiejetnosc()
                    self.punkty_na_klase -= nowy_poziom_skila
                    print(
                        f"\tPodnoszony poziom: {podnoszony_skill.nazwa} na {nowy_poziom_skila} - pozostało: {self.punkty_na_klase} punktów."
                    )
                    continue
                else:
                    print(
                        f"\tNie podniosę skilla {podnoszony_skill.nazwa} - {podnoszony_skill.poziom} bo brak punktów na niego, zostało: {self.punkty_na_klase} punktów"
                    )
                    pass
            else:
                print(
                    f"\tNie można kupić nowego skilla, bo punktów jest: {self.punkty_na_klase}"
                )

            if not any(
                (skill.poziom == 0 and self.punkty_na_klase >= 3)
                or (skill.poziom > 0 and self.punkty_na_klase >= skill.poziom + 1)
                for item in filtered_list
                for skill in item.umiejetnosci
            ):
                print(
                    "Brak wystarczających punktów na podniesienie jakiejkolwiek umiejętności."
                )
                break

        print(f"Koniec kupowania skilli dla klasy")
        return pakiety

    def _sprawdz_pakiety_inne(self, staty):
        kupiono = 0

        # # Losowa liczba pakietów do wykupienia z punktów innych skili:
        pakiety_do_kupienia = self._maksymalna_liczba_pakietow(self.punkty_na_inne)

        print(f"Pakiety do kupienia inne: {pakiety_do_kupienia}")

        # przefiltorwana pakietów lista według klasy:
        filtr_pakiety = [
            pakiet
            for pakiet in pakiety
            if all(umiejetnosc.poziom == 0 for umiejetnosc in pakiet.umiejetnosci)
        ]

        while kupiono < pakiety_do_kupienia and kupiono < len(filtr_pakiety):
            # if kupiono < pakiety_do_kupienia:
            # Utworzenie losowej listy pakietów za każdym obrotem pętli:
            random.shuffle(pakiety)

            wynik = random.choice(staty)
            print(f"wylosowany pakiet: {wynik.nazwa}")

            # Sprawdzenie umiejętności w każdym pakiecie
            # for pakiet in staty:
            for umiejetnosc in wynik.umiejetnosci:
                # Już kupiona umiejętność w pakiecie - przeskakujemy dalej
                if umiejetnosc.poziom != 0:
                    break
            else:
                print(f"KUPIĆ - {wynik.nazwa}")
                kupiono += 1
                wynik.kup_pakiet()
                self.punkty_na_inne -= 5
                print(f"punkty_na_inne po kupnie pakietu: {self.punkty_na_inne}")
                continue
        print(f"Koniec kupowania innych pakietów")
        return pakiety

    def _kupuj_staty_inne(self, staty):
        while self.punkty_na_inne > 1:
            print(f"punkty_na_inne: {self.punkty_na_inne}")

            # Wybrany losowy pakiet
            losowy_pakiet = random.choice(pakiety)

            # Sprawdzenie umiejętności w każdym pakiecie
            print(f"wylosowany pakiet pozostałe: {losowy_pakiet.nazwa}")
            podnoszony_skill = random.choice(losowy_pakiet.umiejetnosci)

            # Już kupiona umiejętność w pakiecie - przeskakujemy dalej
            if podnoszony_skill.poziom == 0 and self.punkty_na_inne >= 3:
                podnoszony_skill.podnies_umiejetnosc()
                self.punkty_na_inne -= 3
                print(
                    f"\tPodnoszony poziom: {podnoszony_skill.nazwa} na 1 - zostało {self.punkty_na_inne} punktów."
                )
                continue

            elif podnoszony_skill.poziom > 0 and self.punkty_na_inne >= 2:
                nowy_poziom_skila = podnoszony_skill.poziom + 1
                if self.punkty_na_inne - nowy_poziom_skila >= 0:
                    podnoszony_skill.podnies_umiejetnosc()
                    self.punkty_na_inne -= nowy_poziom_skila
                    print(
                        f"\tPodnoszony poziom: {podnoszony_skill.nazwa} na {nowy_poziom_skila} - zostało {self.punkty_na_inne} punktów."
                    )
                    continue
                else:
                    print(
                        f"\tNie podniosę skilla {podnoszony_skill.nazwa} - {podnoszony_skill.poziom} bo brak punktów na niego na {self.punkty_na_inne}"
                    )
                    pass
            else:
                print(
                    f"\tNie można kupić nowego skilla, bo punktów jest: {self.punkty_na_inne}"
                )
            if not any(
                (skill.poziom == 0 and self.punkty_na_inne >= 3)
                or (skill.poziom > 0 and self.punkty_na_inne >= skill.poziom + 1)
                for item in pakiety
                for skill in item.umiejetnosci
            ):
                print(
                    "Brak wystarczających punktów na podniesienie jakiejkolwiek umiejętności."
                )
                break

        print(f"Koniec kupowania skilli dla klasy")

        return pakiety

    def statystyki(self):
        # Pierwsze wykupienie pakietów dla klasy:
        staty = self._sprawdz_pakiety_klasa()
        print(f"*********************\n")
        staty = self._kupuj_staty_klasa(staty)
        print(f"*********************\n")

        staty = self._sprawdz_pakiety_inne(staty)
        print(f"*********************\n")
        staty = self._kupuj_staty_inne(staty)
        print(f"*********************\n")

        return staty
