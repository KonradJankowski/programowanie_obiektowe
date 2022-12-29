Zadanie nr 1

Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:

a. Product: nazwa, nazwa kategorii, cena jednostkowa
b. Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), 
    łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
c. Apple: nazwa gatunku, rozmiar, cena za kg
d. Potato: nazwa gatunku, rozmiar, cena za kg
Utwórz kilka obiektów każdej klasy.

 

Zadanie nr 2
Napisz funkcję wypisującą produkt i zamówienie. Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.

 

Zadanie nr 3
Napisz funkcję generującą zamówienie z losową listą produktów na przykład: Produkt-1, Produkt-2 itd.

 

Zadanie nr 4
Podziel projekt - utwórz nowy pakiet shop i przenieś do osobnych modułów (plików) w pakiecie store:

Klasę Apple
Klasę Potato
Klasę Product oraz funkcje generujące i wypisujące produkt
Klasę Order oraz funkcje generujące i wypisujące zamówienie
Utwórz skrypt uruchomieniowy main, który importuje i wykorzystuje powyższe klasy i funkcje