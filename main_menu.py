import os
from python_time.python_time_choises import Python_time_choises as PTC
from german_time.german_time_choises import German_time_choises as GTC
from drinks.drinks_choises import Drinks_choises as DC


class Menu():
    """creating basic menu functions"""

    def is_number(self, options_len):
        """check is input number and in range of menu options"""
        error_msg = f"Wybór musi być liczbą od 1 do {options_len}"
        msg = f"Wprowadź liczbę od 1 do {options_len} aby przejść dalej: "
        try:
            choice = int(input(msg))
            if choice in range(1, options_len+1):
                return choice
            else:
                print(error_msg)
                return self.is_number(options_len)
        except ValueError:
            print(error_msg)
            return self.is_number(options_len)

    def clean(self): return os.system('clear')

    def menu_view(self, options, clear, menu_title):
        print(menu_title)
        for option in options:
            print(option)
        choice = self.is_number(len(options))
        if clear is True:
            self.clean()
        return(choice)


class Main_Menu(Menu):

    def choices(self):
        menu_title = "Główe Menu\n"
        menu_options = ['1. Czas nauki Python',
                        '2. Czas nauki Niemiecki',
                        '3. Historia słodkich napojów',
                        '4. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        if choice == 1:
            x = Python_time_menu()
            x.choices()
        elif choice == 2:
            x = German_time_menu()
            x.choices()
        elif choice == 3:
            x = Drink_menu()
            x.choices()
        elif choice == 4:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices_()


class Python_time_menu(Menu):
    def choices(self):
        menu_title = "Python Czas\n"
        menu_options = ["1. Dodaj czas i datę nauki Pythona",
                        "2. Wyświetl dane",
                        "3. Kasa za czas nauki",
                        "4. Wróć do głównego menu",
                        "5. Zamknij program\n"]
        choice = self.menu_view(menu_options, True, menu_title)
        if choice == 1:
            x = Python_time_menu_choice_1()
            x.choices()
        elif choice == 2:
            x = Python_time_menu_choice_2()
            x.choices()
        elif choice == 3:
            x = Python_time_menu_choice_3()
            x.choices()
        elif choice == 4:
            x = Main_Menu()
            x.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_1(Menu):

    def choices(self):
        menu_options = ['\n1. Dodaj datę i czas',
                        '2. Wróć do poprzedniego menu',
                        '3. Zamknij program\n']
        menu_title = "Dodawanie czasu nauki\n"
        choice = self.menu_view(menu_options, True, menu_title)
        x = PTC()
        y = Python_time_menu_choice_1_1()
        z = Python_time_menu()
        if choice == 1:
            x.choice_1_1()
            y.choices()
        elif choice == 2:
            z.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_1_1(Menu):

    def choices(self):
        menu_title = ""
        menu_options = ['\n1. Dodać kolejne dane',
                        '2. Wrócić do poprzedniego menu',
                        '3. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = PTC()
        y = Python_time_menu()
        if choice == 1:
            x.choice_1_1()
            self.choices()
        elif choice == 2:
            y.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_2(Menu):

    def choices(self):
        menu_title = "Wyświetlanie danych czasu nauki Python\n"
        menu_options = ['\n1. Wyświetl dane wg daty',
                        '2. Wyświetl łączny czas',
                        '3. Wyświetl wykres czasu',
                        '4. Wróć do poprzedniego menu',
                        '5. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = PTC()
        y = Python_time_menu_choice_2()
        z = Python_time_menu()
        if choice == 1:
            x.choice_2_1()
            y.choices()
        elif choice == 2:
            x.choice_2_2()
            y.choices()
        elif choice == 3:
            x.choice_2_3()
            y.choices()
        elif choice == 4:
            z.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_3(Menu):

    def choices(self):
        menu_title = "Wyświetlanie danych dotyczących kasy - Python\n"
        menu_options = ['\n1. Wyświetl kase łącznie',
                        '2. Wyświetl ile jeszcze możesz wypłacić',
                        '3. Wypłać kase',
                        '4. Wróć do poprzedniego menu',
                        '5. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = PTC()
        y = Python_time_menu_choice_3()
        z = Python_time_menu()
        if choice == 1:
            x.choice_3_1()
            y.choices()
        elif choice == 2:
            x.choice_3_2()
            y.choices()
        elif choice == 3:
            x.choice_3_3()
            y.choices()
        elif choice == 4:
            z.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class German_time_menu(Menu):

    def choices(self):
        menu_title = "Niemiecki Czas\n"
        menu_options = ["1. Dodaj czas i datę nauki Niemieckiego",
                        "2. Wyświetl dane",
                        "3. Kasa za czas nauki",
                        "4. Wróć do głównego menu",
                        "5. Zamknij program\n"]
        choice = self.menu_view(menu_options, True, menu_title)
        if choice == 1:
            x = German_time_menu_choice_1()
            x.choices()
        elif choice == 2:
            x = German_time_menu_choice_2()
            x.choices()
        elif choice == 3:
            x = German_time_menu_choice_3()
            x.choices()
        elif choice == 4:
            x = Main_Menu()
            x.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class German_time_menu_choice_1(Menu):

    def choices(self):
        menu_options = ['\n1. Dodaj datę i czas',
                        '2. Wróć do poprzedniego menu',
                        '3. Zamknij program\n']
        menu_title = "Dodawanie czasu nauki\n"
        choice = self.menu_view(menu_options, True, menu_title)
        x = GTC()
        y = German_time_menu_choice_1_1()
        z = German_time_menu()
        if choice == 1:
            x.choice_1_1()
            y.choices()
        elif choice == 2:
            z.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class German_time_menu_choice_1_1(Menu):

    def choices(self):
        menu_title = ""
        menu_options = ['\n1. Dodać kolejne dane',
                        '2. Wrócić do poprzedniego menu',
                        '3. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = GTC()
        y = German_time_menu()
        if choice == 1:
            x.choice_1_1()
            self.choices()
        elif choice == 2:
            y.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class German_time_menu_choice_2(Menu):

    def choices(self):
        menu_title = "Wyświetlanie danych czasu nauki Niemieckiego\n"
        menu_options = ['\n1. Wyświetl dane wg daty',
                        '2. Wyświetl łączny czas',
                        '3. Wyświetl wykres czasu',
                        '4. Wróć do poprzedniego menu',
                        '5. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = GTC()
        y = German_time_menu_choice_2()
        z = German_time_menu()
        if choice == 1:
            x.choice_2_1()
            y.choices()
        elif choice == 2:
            x.choice_2_2()
            y.choices()
        elif choice == 3:
            x.choice_2_3()
            y.choices()
        elif choice == 4:
            z.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class German_time_menu_choice_3(Menu):

    def choices(self):
        menu_title = "Wyświetlanie danych dotyczących kasy Niemiecki\n"
        menu_options = ['\n1. Wyświetl kase łącznie',
                        '2. Wyświetl ile jeszcze możesz wypłacić',
                        '3. Wypłać kase',
                        '4. Wróć do poprzedniego menu',
                        '5. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = GTC()
        y = German_time_menu_choice_3()
        z = German_time_menu()
        if choice == 1:
            x.choice_3_1()
            y.choices()
        elif choice == 2:
            x.choice_3_2()
            y.choices()
        elif choice == 3:
            x.choice_3_3()
            y.choices()
        elif choice == 4:
            z.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Drink_menu(Menu):

    def choices(self):
        menu_title = "Słodkie Napoje\n"
        menu_options = ["1. Dodaj date i info czy piłem słodkie napoje",
                        "2. Wyświetl dane",
                        "3. Kasa za nie picie",
                        "4. Wróć do głównego menu",
                        "5. Zamknij program\n"]
        choice = self.menu_view(menu_options, True, menu_title)
        if choice == 1:
            x = Drink_menu_choice_1()
            x.choices()
        elif choice == 2:
            # x = German_time_menu_choice_2()
            # x.choices()
            print("zawieszone - do rozbudowy\n\n")
            x = Drink_menu()
            x.choices()
        elif choice == 3:
            x = Drink_menu_choice_3()
            x.choices()
        elif choice == 4:
            x = Main_Menu()
            x.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Drink_menu_choice_1(Menu):

    def choices(self):
        menu_options = ['\n1. Dodaj dane',
                        '2. Wróć do poprzedniego menu',
                        '3. Zamknij program\n']
        menu_title = "Dodawanie danych\n"
        choice = self.menu_view(menu_options, True, menu_title)
        x = DC()
        y = Drink_menu_choice_1_1()
        z = Drink_menu()
        if choice == 1:
            x.choice_1_1()
            y.choices()
        elif choice == 2:
            z.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Drink_menu_choice_1_1(Menu):

    def choices(self):
        menu_title = ""
        menu_options = ['\n1. Dodać kolejne dane',
                        '2. Wrócić do poprzedniego menu',
                        '3. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = DC()
        y = Drink_menu()
        if choice == 1:
            x.choice_1_1()
            self.choices()
        elif choice == 2:
            y.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()

# co do tego menu kiedys moze rozbuduje
# o wykres i wyswietlanie danych
# teraz nie mam na to zabardzo pomysłu
# class Drink_menu_choice_2(Menu):

#     def choices(self):
#         menu_title = "Wyświetlanie danych picia\n"
#         menu_options = ['\n1. Wyświetl dane wg daty',
#                         '2. Wyświetl łączny czas',
#                         '3. Wyświetl wykres czasu',
#                         '4. Wróć do poprzedniego menu',
#                         '5. Zamknij program\n']
#         choice = self.menu_view(menu_options, True, menu_title)
#         x = GTC()
#         y = German_time_menu_choice_2()
#         z = German_time_menu()
#         if choice == 1:
#             x.choice_2_1()
#             y.choices()
#         elif choice == 2:
#             x.choice_2_2()
#             y.choices()
#         elif choice == 3:
#             x.choice_2_3()
#             y.choices()
#         elif choice == 4:
#             z.choices()
#         elif choice == 5:
#             exit()
#         else:
#             print('cos poszło nie tak z Main_Menu')
#             self.choices()


class Drink_menu_choice_3(Menu):

    def choices(self):
        menu_title = "Wyświetlanie danych dotyczących kasy - Napoje\n"
        menu_options = ['\n1. Wyświetl kase łącznie',
                        '2. Wyświetl ile jeszcze możesz wypłacić',
                        '3. Wypłać kase',
                        '4. Wróć do poprzedniego menu',
                        '5. Zamknij program\n']
        choice = self.menu_view(menu_options, True, menu_title)
        x = DC()
        y = Drink_menu_choice_3()
        z = Drink_menu()
        if choice == 1:
            x.choice_3_1()
            y.choices()
        elif choice == 2:
            x.choice_3_2()
            y.choices()
        elif choice == 3:
            x.choice_3_3()
            y.choices()
        elif choice == 4:
            z.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()
