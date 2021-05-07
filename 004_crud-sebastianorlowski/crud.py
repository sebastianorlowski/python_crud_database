from tabulate import tabulate
from datetime import date

DATABASE_FILE = "database.txt"


def add_by_hand():
    is_flag = True
    while is_flag:
        print("Prosze podać dane: ")
        print("Id: ", end="")
        identity = input()
        print("Imie: ", end="")
        first_name = input()
        print("Nazwisko: ", end="")
        last_name = input()
        print("Pesel: ", end="")
        pesel = input()
        is_flag = check_id(identity)
        if is_flag is False:
            add_record(identity, first_name, last_name, pesel)
        else:
            is_duplicated_id()


def add_record(identity, first_name, last_name, pesel):
    with open(DATABASE_FILE, mode='a') as database:
        database.write("\n" + str(identity + ";" +
                                  first_name + ";" +
                                  last_name + ";" +
                                  pesel + "\n"))


def add_by_file(file_name):
    if check_id_file(file_name):
        with open(file_name) as file:
            with open(DATABASE_FILE, mode='a') as database:
                database.write(str(file.read()))
    else:
        return False


def display_database():
    record_list = []
    with open(DATABASE_FILE) as file:
        headers = ["ID", "Imię", "Nazwisko", "Pesel"]
        for i in file:
            record_list.append(i.split(";"))
    print(tabulate(record_list, headers, tablefmt="psql"))


def update_record(identifier):
    if not empty_identifier(identifier):
        return False
    if check_id(identifier):
        print("Dane rekordu: ", end="")
        display_record(identifier)
        remove_record(identifier)
        print("Imie: ", end="")
        first_name = input()
        print("Nazwisko: ", end="")
        last_name = input()
        print("Pesel: ", end="")
        pesel = input()
        add_record(identifier, first_name, last_name, pesel)
    else:
        is_notexist_id()
        return False


def remove_record(identifier):
    if empty_identifier(identifier) and check_id(identifier):
        with open(DATABASE_FILE, mode="r") as database:
            lines = database.readlines()
        with open(DATABASE_FILE, mode="w") as database:
            for line in lines:
                record = line.split(";")
                if str(record[0]) != identifier:
                    database.write(line)
            return True
    is_notexist_id()
    return False


def display_record(identifier):
    with open(DATABASE_FILE, mode="r") as database:
        for i in database:
            record = i.split(";")
            if record[0] == identifier:
                print(i)


def convert_pesel():
    pesel_list = []
    with open(DATABASE_FILE, mode="r") as database:
        for line in database:
            record = line.split(";")
            pesel_list.append(str(record[3]))
    return pesel_list


def average_age():
    average = 0
    pesel_list = convert_pesel()
    for p in pesel_list:
        value = convert_date_from_pesel(p)
        average += value
    average /= len(pesel_list)
    average = "{:.2f}".format(average)
    print(average)


def convert_date_from_pesel(pesel):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    if month > 12:
        year = year + 2000
        month = month - 20
    else:
        year = year + 1900
    return compare_dates(year, month, day)


def compare_dates(year, month, day):
    d1 = date(year, month, day)
    d2 = date.today()
    if d1.month < d2.month:
        return d2.year - d1.year
    elif d1.month == d2.month:
        if d1.day <= d2.day:
            return d2.year - d1.year
        else:
            return d2.year - (d1.year + 1)
    else:
        return d2.year - (d1.year + 1)


def convert_count_sex():
    female = 0
    male = 0
    pesel_list = convert_pesel()
    for p in pesel_list:
        number = int(p[9:10])
        if number % 2 == 0:
            female += 1
        else:
            male += 1
    print("Liczba kobiet: ", female)
    print("Liczba mężczyzn: ", male)


def remove_empty_lines():
    database_lines = []
    with open(DATABASE_FILE, "r") as database:
        for d in database:
            if len(d) != 0:
                database_lines.append(d)
    with open(DATABASE_FILE, "w") as database:
        for d in database_lines:
            if not len(d) == 1:
                database.write(d)


def check_id_file(file_name):
    with open(file_name, mode='r') as file:
        for i in file:
            record = i.split(";")
            if check_id(record[0]):
                is_duplicated_id()
                return False
        return True


def check_id(identifier):
    if not empty_identifier(identifier):
        return True
    list_id = []
    with open(DATABASE_FILE, mode="r") as database:
        for i in database:
            record = i.split(";")
            list_id.append(record[0])
        return identifier in list_id


def empty_identifier(identifier):
    if len(identifier) == 0:
        print("Błąd! Pusta wartość!")
        return False
    else:
        return True


def is_duplicated_id():
    print("Błąd! To id już istnieje!")


def is_notexist_id():
    print("Błąd! To id nie istnieje!")





