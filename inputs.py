import sys
import os
import file_handler
import display
# plik raporty jeszcze

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


#print(menu())

def search_menu(cv_list):
    pass

def cv_raport():
    pass
