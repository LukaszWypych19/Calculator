from time import sleep

print('Witaj w programie Kalkulator!')
sleep(1)
print()
                    # czy da się obsluzyc dwa wyjatki dla liczba1 i liczba2 w jednej petli?
                    #     lub napisac ponizsza czesc kodu krocej i prosciej?
while True:
    try:
        liczba1 = int(input('Podaj pierwsza liczbe: '))
        break
    except ValueError:
        print('Błąd! Możesz podawać tylko cyfry.')

while True:
    try:
        liczba2 = int(input('Podaj drugą liczbe: '))
        break
    except ValueError:
        print('Błąd! Możesz podawać tylko cyfry.')

nr_dzialania = 0
lista_wynikow = []

#                         przeniesienie do petli naprawilo blad polegajacy na tym ze nie wykonywaly sie
#                         dzialania na nowopodanych liczbach - jest jakis inny sposob?
# def mnozenie(liczba1, liczba2):
#     return liczba1 * liczba2
# wynik_mnozenia = mnozenie(liczba1, liczba2)
#
# def dzielenie():
#     return liczba1/liczba2
# wynik_dzielenia = dzielenie()
#
# def dodawanie():
#     return liczba1 + liczba2
# wynik_dodawania = dodawanie()
#
# def odejmowanie():
#     return liczba1 - liczba2
# wynik_odejmowania = odejmowanie()

while nr_dzialania != 7:
    def mnozenie():
        return liczba1 * liczba2
    wynik_mnozenia = mnozenie()

    def dzielenie():
        return liczba1 / liczba2
    wynik_dzielenia = dzielenie()

    def dodawanie():
        return liczba1 + liczba2
    wynik_dodawania = dodawanie()

    def odejmowanie():
        return liczba1 - liczba2
    wynik_odejmowania = odejmowanie()

    if nr_dzialania == 1:
        print('-' * 20)
        print('Wynik mnożenia to: ', wynik_mnozenia)
        print('-' * 20)
        lista_wynikow.append(wynik_mnozenia)

    if nr_dzialania == 2:
        print('-' * 20)
        print('Wynik dzielenia to: ', wynik_dzielenia)
        print('-' * 20)
        lista_wynikow.append(wynik_dzielenia)

    if nr_dzialania == 3:
        print('-' * 20)
        print('Wynik dodawania to: ', wynik_dodawania)
        print('-' * 20)
        lista_wynikow.append(wynik_dodawania)

    if nr_dzialania == 4:
        print('-' * 20)
        print('Wynik odejmowania to: ', wynik_odejmowania)
        print('-' * 20)
        lista_wynikow.append(wynik_odejmowania)

    if nr_dzialania == 5:
        while True:
            try:
                liczba1 = int(input('Podaj pierwsza liczbe: '))
                break
            except ValueError:
                print('Błąd! Możesz podawać tylko cyfry.')

        while True:
            try:
                liczba2 = int(input('Podaj drugą liczbe: '))
                break
            except ValueError:
                print('Błąd! Możesz podawać tylko cyfry.')

    if nr_dzialania == 6:
        print('Zakonczyles dzialanie kalkulatora. Dziekuje !')
        print(lista_wynikow)
        break
    print()
    print('Możesz wykonać jedno z poniższych działań: ')
    lista_dzialan = ['1. Mnożenie',
                     '2. Dzielenie',
                     '3. Dodawanie',
                     '4. Odejmowanie',
                     '5. Nowe liczby',
                     '6. Zakończ'
                     ]
    for i in lista_dzialan:
        print(i)
    nr_dzialania = int(input('Podaj numer działania jakie chcesz wykonać na podanych liczbach: '))
    sleep(1)
    print()

            # co zrobic zeby kazda podana liczba po zatwierdzeniu enterem zapisywalo sie do pliku?
            # co zrobic zeby do pliku zapisywalo sie cale dzialanie czyli np 3 * 4 = 12 ?

plik = open('../kalkulator_wyniki.txt', 'w+')
for i in range(len(lista_wynikow)):
    plik.write(str(lista_wynikow[i]) + '\n')
plik.close()
