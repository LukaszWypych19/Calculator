from time import sleep

liczba1 = int(input('Podaj pierwsza liczbe: '))
liczba2 = int(input('Podaj drugą liczbe: '))
print('Podane przez Ciebie liczby to: ', liczba1, ' i ', liczba2)
print()
nr_dzialania = 0

# plik = open('kalkulator.txt', 'w+')
# plik.write('Filip')
# plik.close()

def mnozenie():
    print('Wynik mnożenia to: ',liczba1 * liczba2)
def dzielenie():
    print('Wynik dzielenia to: ',liczba1/liczba2)
def dodawanie():
    print('Wynik dodawania to: ',liczba1+liczba2)
def odejmowanie():
    print('Wynik odejmowania to: ',liczba1-liczba2)

sleep(2)


while nr_dzialania != 7:
    if nr_dzialania == 1:
        mnozenie()

    if nr_dzialania == 2:
        dzielenie()

    if nr_dzialania == 3:
        dodawanie()

    if nr_dzialania == 4:
        odejmowanie()

    if nr_dzialania == 5:
        liczba1 = int(input('Podaj pierwsza liczbe: '))
        liczba2 = int(input('Podaj drugą liczbe: '))
        print('Podane przez Ciebie liczby to: ', liczba1, ' i ', liczba2)
    if nr_dzialania == 6:
        print('Zakonczyles dzialanie kalkulatora. Dziekuje !')
        break
    print('Możesz wykonać jedno z poniższych działań: ')
    print('1. Mnożenie')
    print('2. Dzielenie')
    print('3. Dodawanie')
    print('4. Odejmowanie')
    print('5. Nowe liczby')
    print('6. Zakończ')
    print()
    nr_dzialania = int(input('Podaj numer działania jakie chcesz wykonać na podanych liczbach: '))

# lista_wynikow = []
# for wynik in lista_wynikow:
#     lista_wynikow.append(liczba1)
#     lista_wynikow.append(liczba2)
#     print(lista_wynikow)
