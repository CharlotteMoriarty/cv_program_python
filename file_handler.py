def import_cv(filename="cv.txt"):
    try:
        with open(filename,"r") as data_import:
            cv_list = []
            for line in data_import:
                cv_list.append(line)
            cv_list = [x.strip().split(",") for x in cv_list]

            print("\t\t Zaimportowano plik {}".format(filename))

            return cv_list
    except FileNotFoundError:
        print("Nie znaleziono pliku! ")

