import sys
import os
import file_handler
import display
import cv_raport


def menu():
    cv_list = []
    loop_handling = True
    while loop_handling:
        print("\n\t\t**************CV MENU************\n")

        choice = input("""
                1: Import cv
                2: Wyświetlanie cv
                3: Wyszukiwanie danych
                4: Raport 
                5: Wyjście
                
                Wprowadź wybór:  
        """)

        if choice == "1":
            os.system("clear")
            display.logo_print()
            cv_list = file_handler.import_cv("cv.txt")
        elif choice == "2":
            os.system("clear")
            display.logo_print()
            display.display_table_header()
            for cv in cv_list:
                display.display_cv_to_print(cv)
        elif choice == "3":
            os.system("clear")
            display.logo_print()
            search_menu(cv_list)
        elif choice == "4":
            os.system("clear")
            display.logo_print()
            cv_raport.display_raport(cv_list)
        elif choice == "5":
            os.system("clear")
            print("""\033[1;38m
            
            01000111 01101111 01101111 01100100 01100010 01111001 01100101 


            \033[1;m""")
            sys.exit()
        else:
            print("Spróbuj ponownie")


def search_menu(cv_list):
    loop_handling = True
    while loop_handling:
        search_choice = input("""
                        1: Wyszukaj po kategorii
                        2: Wyszukaj po roku rozpoczęcia
                        3: Wyszukaj po nazwie stanowiska
                        4: Wyszukaj po nazwie firmy
                        5: Wyjście


                        Wpisz wybraną opcję: """)

        if search_choice == '1':
            os.system("clear")
            display.logo_print()
            genre_search(cv_list)
        elif search_choice == '2':
            os.system("clear")
            display.logo_print()
            year_search(cv_list)

        elif search_choice == '3':
            os.system("clear")
            display.logo_print()
            position_search(cv_list)
        elif search_choice == '4':
            os.system("clear")
            display.logo_print()
            company_search(cv_list)
        elif search_choice == '5':
            os.system("clear")
            display.logo_print()
            menu()
        else:
            print("Opcja od 1 do  5.")


def position_search(input_cv):
    loop_handling = True
    while loop_handling:
        ask_user_about_position_name = input("Wpisz interesujące Cię stanowisko/ pełna nazwa/ : ").title()
        positions = []
        for cv_data in input_cv:
            positions.append(cv_data[0])
        if ask_user_about_position_name in positions:
            display.display_table_header()
            for cv in input_cv:
                if ask_user_about_position_name in cv[0]:
                    display.display_cv_to_print(cv)
            loop_handling = False
        else:
            print("Brak stanowiska na zaimportowanej liście.")


def company_search(input_cv):
    loop_handling = True
    while loop_handling:
        ask_about_company = input("test").title()
        company = []
        for cv_data in input_cv:
            company.append(cv_data[1])
        if ask_about_company in company:
            display.display_table_header()
            for cv in input_cv:
                if ask_about_company in cv[1]:
                    display.display_cv_to_print(cv)
            loop_handling = False
        else:
            print("cos")


def genre_search(input_cv):
    loop_handling = True
    while loop_handling:
        ask_user_about_genre = input("Wpisz interesującą Cię kategorię: ")
        genres = []
        for cv_data in input_cv:
            genres.append(cv_data[3])
        if ask_user_about_genre in genres:
            display.display_table_header()
            for cv in input_cv:
                if ask_user_about_genre in cv[3]:
                    display.display_cv_to_print(cv)
            loop_handling = False
        else:
            print("Brak kategorii! ")


def year_search(input_cv):
    loop_handling = True
    while loop_handling:
        year_range = input("Wpisz interesujący Cię rok (yyyy-yyyy): ")
        if "-" in year_range:
            year_range = year_range.split("-")
            year_range = [int(year) for year in year_range]
            display.display_table_header()
            for cv in input_cv:
                if int(cv[2]) in range(year_range[0], year_range[1] + 1):
                    display.display_cv_to_print(cv)
                else:
                    print("Brak danych w tym okresie")
                    break
            loop_handling = False
        else:
            print("Wpisz interesujący Cię rok (yyyy-yyyy):  ")


