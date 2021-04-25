# Zadanie nr 4 - CRUD

| Termin oddania | Punkty     |
|----------------|:-----------|
|    27.04.2021 23:00 |   10        |

--- 
Przekroczenie terminu o **n** zajęć wiąże się z karą:
- punkty uzyskania za realizację zadania są dzielone przez **2<sup>n</sup>**.

--- 
Zadanie polega na stworzeniu modułu, który dostarczy nam funkcjanolność bazy danych z zakresu CRUD (create, read, update, delete). Struktura bazy danych:
id;imię;nazwisko;pesel.

Domyślnie po włączneniu skryptu baza jest pusta.
## CREATE [3 pkt]
Użytkownik ma dwie możliwość wprowadzenia nowych rekorów do bazy.
1. Wczytanie z pliku tekstowego (przykładowy plik został dołączony do repozytorium - data.txt).
2. Wpisanie odpowienich wartości w konsoli.

Przed dodaniem rekordu do bazy należy odpowiednio sprawdzić unikatowość id.

## READ [1 pkt]
Użytkownik powinien mieć możliwość odczytania całej zawartośći bazy danych w czytelny sposób.

## UPDATE [2 pkt]
Użytkownik proszony jest o podanie ID dla którego chce dokonać zmiany, a następnie o podanie nowych wartości. Jeżli podane ID nie występuje w bazie, powinien pojawić się odpowiedni komunikat.

## DELETE [2 pkt]
Usuwanie rekordu na podstawie podanego przez użytkownika ID. Jeżli podane ID nie występuje w bazie, powinien pojawić się odpowiedni komunikat.

## DODATKI [2 pkt]
1. Funkcja licząca średni wiek osób w bazie danych na podstawie numeru pesel.
2. Funkcja zwracająca liczbę kobiet i mężczyzn w bazie danych na podstawie numeru pesel.

## Uwagi
1. Zakładamy, że id jest kluczem podstawowym i unikatowym.
2. Opis operacji na plikach [Python File I/O](https://www.programiz.com/python-programming/file-operation).
3. Wszystkie funkcje powinny być napisane w storzownym module. Program główny powinien jedynie z nich odpowiednio korzystać.
