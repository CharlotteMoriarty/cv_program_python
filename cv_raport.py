import inputs
import display
import os


def display_raport(cv_list):
    os.system("clear")
    print("Raport")
    print("Liczba dostępnych pozycji na liście {}".format(count_genres(cv_list)))
    #print("Liczba dostępnych kategorii na liście {} ".format(count_category(cv_list)))


def count_genres(input_list):
    genres_number = len(input_list)
    #genres_to_compare = input_list[0][3]
    genres_to_compare = input_list[0][1]

    for line in input_list:
        if genres_to_compare == line[3]:
            genres_number -= 1
    return genres_number


def count_category(input_list):
    pass
