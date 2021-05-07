import crud

isFlag = True

print("Program baza danych")

with open(crud.DATABASE_FILE, "w") as database:
    database.truncate()

while isFlag:

    print("1. Wprowadź dane z pliku tekstowego")
    print("2. Wprowadź dane ręcznie")
    print("3. Odczyt bazy danych")
    print("4. Edycja rekordu")
    print("5. Usuniecie rekordu")
    print("6. Średni wiek osób")
    print("7. Liczba kobiet i mężczyzn")
    print("8. Koniec programu")

    crud.remove_empty_lines()
    print("Wybór: ", end="")
    number = int(input())

    if number == 1:
        print("Wprowadź nazwę pliku: ", end="")
        file_name = input()
        crud.add_by_file(file_name)
    elif number == 2:
        crud.add_by_hand()
    elif number == 3:
        crud.display_database()
    elif number == 4:
        print("Podaj id: ", end="")
        identifier = input()
        crud.update_record(identifier)
    elif number == 5:
        print("Podaj id rekordu do usuniecia: ")
        identifier = input()
        crud.remove_record(identifier)
    elif number == 6:
        crud.average_age()
    elif number == 7:
        crud.convert_count_sex()
    elif number == 8:
        isFlag = False


