# WISIELEC
# GRA POLEGAJACA NA ODGADYWANIU SŁÓW
import sys
import random
import time

no_of_tries = 5  # zmienna przechowująca liczbe żyć
used_letter = []   # tablica przechowująca użyte litery
user_word = []     # tablica przechowująca stan odgadniecia hasła w trakcie zgadywania

words = ["kamila","ola","zosia","tomek","agnieszka", "ireneusz", "julia", "andrzej","piotr", "karol","oliwia","zenek","mariola","maria"
        ,"wojciech","krzysztof","jacek","malgorzata","jan","ryszard","waldemar","barabra", "beata", "ewa", "jurek"]     # zmienna przechowująca hasło do odgadnięcia

def enter_letter(): #funkcja odpowiedzialna za walidacje i podawanie liter
    letter = input("Podaj literę: ").lower() # jezeli uzytkownik wprowadzi wielka litere to zamienia ją na małą


    if len(letter) != 1 or letter >'z' or letter <'a':
        print("Podałeś zły znak, bądź ciąg znaków!")

        while len(letter) != 1 or letter >'z' or letter <'a':
            letter = input("Podaj literę ponownie: ")

    return letter

def check_repetition (letter,used_letter): # funkcja odpowiedzialna za sprawdzanie czy uzytkownik nie wprowadził tej samej litery dwukrotnie

    if all(char != letter for char in used_letter):
        print("Podano prawidłową literę!")
        return True
    else:
        print("Ta litera została podana wcześniej!")
        return False

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word: #porownuje litere podana przez uzytkownika z ta stojący pod danym indekscie w słowie word
            indexes.append(index)  # jezeli litery sa takie same index komorki zapisuje do listy indexes

    return indexes

def show_state_of_game():   # funkcja odpowiedzialna za wyświetlanie stanu  gry
    print()
    print(user_word)
    print("Pozostało prób:",no_of_tries)
    print("Użyte litery:", used_letter)

def restart_stats(no_of_tries, used_letter, user_word,):
    no_of_tries = 5  # zmienna przechowująca liczbe żyć
    used_letter = []  # tablica przechowująca użyte litery
    user_word = []  # tablica przechowująca stan odgadniecia hasła w trakcie zgadywania

    for _ in word:
        user_word.append("_")  # _ _ _ _ _ //zakrywa hasło do zgadywania
    return no_of_tries, used_letter,user_word

def show_menu(): #FUNKCJA WYŚWIETLAJĄCA MENU GŁÓWNE GRY
    print("Witaj w MENU GŁÓWNYM:")
    print("1. ZGADYWANIE IMION")
    print("2. 100 ŻYĆ")
    print("3. ZGADUJ ALBO GIŃ")
    print("4. HISTORIA ROZGRYWEK")
    print("5. INFORMACJE O TRYBACH GRY I TWÓRCACH")
    print("6. WYJŚCIE Z GRY")

def select_option(): #DO POPRAWY BLOK TRY, EXCEPT *

    try:
        choice = int(input("PODAJ OPCJĘ:"))

        if choice > 6 or choice < 1:

            print("OPCJA O TYM NUMERZE NIE ISTNIEJE!")

        while  choice > 6 or choice < 1:
            choice = int (input("Podaj OPCJĘ PONOWNIE: "))

        return choice
    except :
        print("Musisz podać opcję oznaczoną odpowiednią cyfrą!!!")

def choose_number_of_tries():
    try:
        chance = int(input("Podaj liczbę żyć, które chcesz mieć:"))

        while chance < 1:
            chance = int(input("Podaj liczbę żyć ponownie:"))

        return chance
    except :
        print("TO MUSI BYC DODATNIA CYFRA A NIE ZNAK!!!")
        choose_number_of_tries()


def choose_level():
    try:
        poziom = int(input("WYBIERZ POZIOM TRUDNOŚCI; 1-IZI IZI ,2-ESA, 3-NORMAL:"))

        while poziom > 3 or poziom < 1:
            poziom = int(input("Podaj poziom jeszcze raz; 1-IZI IZI,2-ESA, 3-NORMAL:"))

        return poziom

    except:
        print("TO MUSI BYĆ LICZBA Z ZAKERSU 1-3, A NIE ZNAK!!!")
        choose_level()


def show_vowels(user_word, word): #funkcja odsłaniająca w hasle samogłoski

    used_letter = ['a','e','i','o','u','y']


    for index, letter_in_word in enumerate(word):
        if letter_in_word == 'a' or letter_in_word == 'e'or letter_in_word == 'i'or letter_in_word == 'o'or letter_in_word == 'u'or letter_in_word == 'y':
            user_word[index] = letter_in_word



    return user_word, used_letter

def show_first_and_last(user_word, word):
    used_letter = []
    user_word[0] = word[0]
    user_word[len(word)-1] = word[len(word)-1]
    used_letter.append(word[0])
    used_letter.append(word[len(word)-1])

    return user_word, used_letter


print("WITAJ W GRZE WISIELEC!!!")
print()


while True: # petla wykonująca sie w nieskonczonosc

    show_menu()
    choice = select_option()

    if choice == 1:
        word = words[random.randint(0, 10)]
        no_of_tries, used_letter,user_word = restart_stats(no_of_tries,used_letter,user_word)


        letter = enter_letter() #uzytkownik podaje dowolną litere

        while True:

            if check_repetition(letter,used_letter) == True :
                used_letter.append(letter)          # podana litera zapisywana jest do listy uzytych liter

                # wywołanie funkcji find_indexes aby znalezc pod jakimi indeksami w hasle znajduje sie litera podana przez usera
                found_indexes = find_indexes(word,letter)  # funkcja powyzej przypisujaca znalezione indeksy do nowej zmiennej

                if len(found_indexes) == 0:
                    print("Nie ma takiej litery")
                    no_of_tries -= 1

                if no_of_tries == 0:
                    print("KONIEC GRY")
                    sys.exit(0)
                else:
                    for index in found_indexes:
                        user_word[index] = letter

                    if "".join(user_word) == word:
                        print("BRAWO!!! ODGADŁES SŁOWO")
                        print()
                        restart = input('CZY CHCIAŁBYŚ ZAGRAĆ PONOWNIE?(tak/nie): ')
                        if restart == 'tak':
                            no_of_tries, used_letter,user_word = restart_stats(no_of_tries,used_letter,user_word)
                            break
                        else:
                            print("!!!WRÓĆ SZYBKO!!!")
                            sys.exit(0)


                show_state_of_game()

                letter = enter_letter()  # uzytkownik podaje dowolną litere

            else:
                letter = enter_letter()

    elif choice == 2:
        print()
        print("WYBRANO OPCJĘ DRUGĄ")

        word = words[random.randint(0, 10)]
        no_of_tries, used_letter, user_word = restart_stats(no_of_tries, used_letter, user_word) #przywracanie ustawien jak w zwykłej grze
        no_of_tries = choose_number_of_tries() # wybor ilosci życ


        level = choose_level()

        if level == 1 : # ułatawiony tryb gry pokazujący w zgadywanym hasle wszystkie samogłoski

            user_word, used_letter = show_vowels (user_word,word)

            letter = enter_letter()  # uzytkownik podaje dowolną litere

            while True:

                if check_repetition(letter, used_letter) == True:
                    used_letter.append(letter)  # podana litera zapisywana jest do listy uzytych liter

                    # wywołanie funkcji find_indexes aby znalezc pod jakimi indeksami w hasle znajduje sie litera podana przez usera
                    found_indexes = find_indexes(word,
                                                 letter)  # funkcja powyzej przypisujaca znalezione indeksy do nowej zmiennej

                    if len(found_indexes) == 0:
                        print("Nie ma takiej litery")
                        no_of_tries -= 1

                    if no_of_tries == 0:
                        print("KONIEC GRY")
                        sys.exit(0)
                    else:
                        for index in found_indexes:
                            user_word[index] = letter

                        if "".join(user_word) == word:
                            print("BRAWO!!! ODGADŁES SŁOWO")
                            print()
                            restart = input('CZY CHCIAŁBYŚ ZAGRAĆ PONOWNIE?(tak/nie): ')
                            if restart == 'tak':
                                no_of_tries, used_letter, user_word = restart_stats(no_of_tries, used_letter, user_word)
                                break
                            else:
                                print("!!!WRÓĆ SZYBKO!!!")
                                sys.exit(0)

                    show_state_of_game()

                    letter = enter_letter()  # uzytkownik podaje dowolną litere

                else:
                    letter = enter_letter()



        elif level == 2:
            user_word, used_letter = show_first_and_last(user_word, word)

            letter = enter_letter()  # uzytkownik podaje dowolną litere

            while True:

                if check_repetition(letter, used_letter) == True:
                    used_letter.append(letter)  # podana litera zapisywana jest do listy uzytych liter

                    # wywołanie funkcji find_indexes aby znalezc pod jakimi indeksami w hasle znajduje sie litera podana przez usera
                    found_indexes = find_indexes(word,letter)  # funkcja powyzej przypisujaca znalezione indeksy do nowej zmiennej

                    if len(found_indexes) == 0:
                        print("Nie ma takiej litery")
                        no_of_tries -= 1

                    if no_of_tries == 0:
                        print("KONIEC GRY")
                        sys.exit(0)
                    else:
                        for index in found_indexes:
                            user_word[index] = letter

                        if "".join(user_word) == word:
                            print("BRAWO!!! ODGADŁES SŁOWO")
                            print()
                            restart = input('CZY CHCIAŁBYŚ ZAGRAĆ PONOWNIE?(tak/nie): ')
                            if restart == 'tak':
                                no_of_tries, used_letter, user_word = restart_stats(no_of_tries, used_letter, user_word)
                                break
                            else:
                                print("!!!WRÓĆ SZYBKO!!!")
                                sys.exit(0)

                    show_state_of_game()

                    letter = enter_letter()  # uzytkownik podaje dowolną litere

                else:
                    letter = enter_letter()

        elif level == 3:
            letter = enter_letter()  # uzytkownik podaje dowolną litere

            while True:

                if check_repetition(letter, used_letter) == True:
                    used_letter.append(letter)  # podana litera zapisywana jest do listy uzytych liter

                    # wywołanie funkcji find_indexes aby znalezc pod jakimi indeksami w hasle znajduje sie litera podana przez usera
                    found_indexes = find_indexes(word,
                                                 letter)  # funkcja powyzej przypisujaca znalezione indeksy do nowej zmiennej

                    if len(found_indexes) == 0:
                        print("Nie ma takiej litery")
                        no_of_tries -= 1

                    if no_of_tries == 0:
                        print("KONIEC GRY")
                        sys.exit(0)
                    else:
                        for index in found_indexes:
                            user_word[index] = letter

                        if "".join(user_word) == word:
                            print("BRAWO!!! ODGADŁES SŁOWO")
                            print()
                            restart = input('CZY CHCIAŁBYŚ ZAGRAĆ PONOWNIE?(tak/nie): ')
                            if restart == 'tak':
                                no_of_tries, used_letter, user_word = restart_stats(no_of_tries, used_letter, user_word)
                                break
                            else:
                                print("!!!WRÓĆ SZYBKO!!!")
                                sys.exit(0)

                    show_state_of_game()

                    letter = enter_letter()  # uzytkownik podaje dowolną litere

                else:
                    letter = enter_letter()


    elif choice == 3:
        word = words[random.randint(0, 10)]
        no_of_tries, used_letter, user_word = restart_stats(no_of_tries, used_letter, user_word)
        no_of_tries = 1
        letter = enter_letter()  # uzytkownik podaje dowolną litere

        while True:

            if check_repetition(letter, used_letter) == True:
                used_letter.append(letter)  # podana litera zapisywana jest do listy uzytych liter

                # wywołanie funkcji find_indexes aby znalezc pod jakimi indeksami w hasle znajduje sie litera podana przez usera
                found_indexes = find_indexes(word,
                                             letter)  # funkcja powyzej przypisujaca znalezione indeksy do nowej zmiennej

                if len(found_indexes) == 0:
                    print("Nie ma takiej litery")
                    no_of_tries -= 1

                if no_of_tries == 0:
                    print("KONIEC GRY")
                    sys.exit(0)
                else:
                    for index in found_indexes:
                        user_word[index] = letter

                    if "".join(user_word) == word:
                        print("BRAWO!!! ODGADŁES SŁOWO")
                        print()
                        restart = input('CZY CHCIAŁBYŚ ZAGRAĆ PONOWNIE?(tak/nie): ')
                        if restart == 'tak':
                            no_of_tries, used_letter, user_word = restart_stats(no_of_tries, used_letter, user_word)
                            break
                        else:
                            print("!!!WRÓĆ SZYBKO!!!")
                            sys.exit(0)

                show_state_of_game()

                letter = enter_letter()  # uzytkownik podaje dowolną litere

            else:
                letter = enter_letter()

    elif choice == 4:
        print("TEGO TRZA JESZCZE SIE NAUCZYC")
        sys.exit(0)

    elif choice == 5:
        file = open('tworca.txt','r')
        print()
        for linia in file:
            print(linia.strip())

        time.sleep(5)

        file.close()
        print()
        print()

    elif choice == 6:
        print("DZIĘKI ZA GRĘ")
        sys.exit(0)

    else:
        print("BŁĘDNY NUMER. PODAJ OPCJĘ JESZCZE RAZ!!!")
        print()






# dodać walidacje co wprowadza uzytkownik, czy to jest litera słowo liczba itd. //zrobione
# nie pozwolic uzytkownikowi wpisac 2 razy ta samą litere // zrobione
# umozliwic restart gry po zakonczeniu // zrobione
# spytac uzytkownika ile chce szans
# dac mozliwosc wyboru poziomu trudnosci

