#for

#zad1
# Napisz program, który wyświetli kolejne liczby całkowite od 5 do 10.
# for i in range(5,11):
#     print("Liczba: ",i)

# #zad2
# Napisz program, który wyświetli kolejno wszystkie liczby parzyste z przedziału [2,20].
# for i in range(2, 21, 2):
#     print("Liczba: ", i)

#zad3
# Napisz program, który wyświetli kolejne liczby całkowite od 0 do n, dla n podanego
# przez użytkownika.

# liczba = input("Podaj liczbe: ")
# for i in range(0, int(liczba)+1):
#     print("Liczba: ", i)

#zad4
# Napisz program, który wyświetli sumę liczb z przedziału od 1 do n, dla n podanego przez
# użytkownika.

# liczba = int(input("Podaj liczbe: "))
# suma=0
# for i in range(0, liczba+1, 1):
#     suma=suma+i
# print("Suma = " ,suma) # tutaj nie moze byc wciecia!!!!

#zad5
# #Napisz program, który wyświetli na ekranie drugie potęgi liczb od 1 do n, dla n podanego
#przez użytkownika, np. dla podanej przez użytkownika liczby 6 należy wyświetlić:
# liczba = input("Podaj liczbe: ")
# for i in range(1, int(liczba)+1, 1):
#     print(str(i) +" * "+str(i) +" = "+ str(i*i))

#zad6
# Napisz program, który wyświetla na ekranie liczby według poniższego schematu (ilość
# liczb wczytujemy z klawiatury), np. dla podanej przez użytkownika liczby 5, należy
# wyświetlić:

# liczba = int(input("Podaj liczbe: "))
# for i in range(0, liczba*3, 3):
#     print(i)

#zad7
# Napisz program, który wyświetli sumę cyfr liczby podanej przez użytkownika.

# liczba = input("Podaj liczbe: ")
# suma = 0
# for i in range(0, len(liczba)):
#     suma += int(liczba[i])
# print("Suma Twojej liczby to:",suma)


#Petla WHILE

#Zad1
#Rozbuduj zadanie 7 z pętli for w taki sposób, aby program pobierał od użytkownika jedynie
#dodatnią liczbę całkowitą. Wskazówka:

# number = input("Podaj liczbę")
# suma=0
# while int(number) < 0:
#     number = input("Spróbuj jeszcze raz")
# else:
#     for i in range(0, len(number)):
#         suma += int(number[i])
# print("Suma Twojej liczby to:",suma)

#Zad2
#Napisz program, który wyświetli kolejne liczby całkowite od 1 do 15.
# liczba = 1
# while liczba <= 15:
#     print (liczba)
#     liczba += 1

#Zad3
#Napisz program, który wyświetli kolejne liczby od 1 do n, dla n podanego przez użytkownika.

# i = 1
# liczba = int(input("Podaj liczbe: "))
# while i < liczba+1:
#     print(i)
#     i+=1

#Zad4
#Napisz program, który wyświetli kolejne liczby całkowite z przedziału podanego przez użytkownika.

# liczba1 = int(input("Poaj pierwsza liczbe: "))
# liczba2 = int(input("Podaj druga liczbe: "))
# while(liczba1<=liczba2):
#     print(liczba1)
#     liczba1+=1

#Zad5
#Rozbuduj zadanie 4 w taki sposób, aby uniemożliwić użytkownikowi podanie niepoprawnego przedziału.

# liczba1 = int(input("Poaj pierwsza liczbe: "))
# liczba2 = int(input("Podaj druga liczbe: "))
# if (liczba1 > liczba2):
#     print("Nieprawidlowy przedzial")
# else:
#     while(liczba1<=liczba2):
#         print(liczba1)
#         liczba1+=1

#Zad6
# Napisz program, który na podstawie wczytanego numeru miesiąca,
# wyświetla jego nazwę słownie. Program powinien ponawiać wczytywanie,
# dopóki podany przez użytkownika numer nie będzie poprawnym numerem miesiąca.

# dzien = int(input("Podaj numer miesiaca: "))
# while dzien < 1 or dzien > 12:
#     dzien = int(input(print("Nieprawidlowy zakres, sprobuj jeszcze raz: ")))
# else:
#     if dzien == 1:
#         print("Styczen")
#     elif dzien == 2:
#         print("Luty")
#     elif dzien == 3:
#         print("Marzec")
#     elif dzien == 4:
#         print("Kwiecien")
#     elif dzien == 5:
#         print("Maj")
#     elif dzien == 6:
#         print("Czerwiec")
#     elif dzien == 7:
#         print("Lipiec")
#     elif dzien == 8:
#         print("Sierpien")
#     elif dzien == 9:
#         print("Wrzesien")
#     elif dzien == 10:
#         print("Pazdziernik")
#     elif dzien == 11:
#         print("Listopad")
#     elif dzien == 12:
#         print("Grudzien")

#Zad7
#Napisz program, który wczytuje liczby rzeczywiste aż do momentu, gdy podana liczba jest równa zero,
# a następnie wyświetla na ekranie sumę i średnią arytmetyczną tych liczb.

# b = 0
# i = []
# liczba = float(input("Podaj liczbe(wpisanie 0 skutkuje zakonczeniem): "))
# while(liczba!=0):
#     b+=liczba
#     i.append(liczba)
#     srednia = len(i)
#     liczba = float(input("Podaj liczbe(wpisanie 0 skutkuje zakonczeniem): "))
# print("Suma = ",b,". Srednia = ", b/srednia)

#Zad8
# Napisz program, który oblicza pole i obwód kwadratu o długości boku podanym przez użytkownika.
# Program jako dane powinien przyjmować wyłącznie liczby dodatnie.

# bok = float(input("Podaj dlugosc boku kwadratu w centymetrach: "))
# while(bok > 0):
#     pole=(bok*bok)
#     obwod=bok*4
#     print("Pole kwadratu wynosi: ",pole,"cm. Obwod kwadratu wynosi: ",obwod," cm")
#     break
# else:
#     print("Liczba musi byc dodatnia!")



#Petle zagniezdzone

#Zad1
#Napisz program, który wyświetla kwadrat 5 x 5 ze znaków #, jak poniżej:
# rozmiar = int(input(print("Podaj rozmiar: ")))
# znak = input(print("Podaj znak: "))
# for i in range(1, rozmiar+1):
#     for j in range(rozmiar, rozmiar+1):
#         print(j * znak)

#Zad2
# Napisz program, który wyświetla tabliczkę mnożenia rozmiaru 10 x 10. Zadbaj o to, by
# # kolumny wyrównane były do prawej krawędzi. Wskazówka: wyświetlanie tekstu na
# # ekranie odbywa się linia po linii, od lewej do prawej strony ekranu.

# rozmiar = int(input(print("Podaj rozmiar tabliczki mnożenia(np. 3 to mnożenie do 30): ")))
# for x in range(1,rozmiar+1):
#       print()
#       for y in range(1,11):
#             print ("%3i" % (x*y), end= " ")

#Zad3
#Napisz program, który wyświetli poniższy trójkąt z gwiazdek (wysokość 10):

# rozmiar = int(input(print("Podaj rozmiar: ")))
# znak = input(print("Podaj znak:"))
# for i in range(1,rozmiar+1):
#     print(i*znak)

#Zad4
# Napisz program, który wyświetli poniższy trójkąt z gwiazdek (wysokość 10):

# rozmiar = int(input(print("Podaj rozmiar: ")))
# znak = input(print("Podaj znak: "))
# for i in range(rozmiar,0,-1):
#         print(i*znak)

#Zad5
#Zastosowane do poprzednich

#Zad6
#Zastosowane do poprzednich

#Zad7
# Zadanie o wyższym poziomie trudności: liczba armstronga (narcystyczna) to liczba, która
# jest sumą n-tych potęg swoich cyfr, gdzie n oznacza ilość cyfr w danej liczbie. Np.:
# 153 1 5 3 1 125 27 3 3 3 = + + = + +
# Napisz program, która dla dowolnej, wczytanej z klawiatury liczby sprawdzi, czy jest ona
# liczbą armstronga

liczba = int(input("Podaj liczbe : "))
obl = 0
n = 0
przechowaj = liczba
while (przechowaj != 0):
    przechowaj =int(przechowaj/10)
    n = n + 1
przechowaj = liczba
while (przechowaj != 0):
    reszta = przechowaj%10
    obl = obl + reszta**n
    przechowaj = int(przechowaj/10)
if(obl == liczba):
    print(liczba,"jest liczba Armstronga")
else:
    print(liczba,"nie jest liczba Armstronga")