from ui import Ui
from csv_okuma import veri_okuma

menu = Ui(["ülkelerdeki felaketleri lsitele",
           "belirli aralıktaki felaketleri listele",
           "belirlenen tipteki felaketleri listele",
           "belirlenen kıtalardaki felaketleri listele",
           "çıkış"])
veri = veri_okuma()


while True:
    menu.Show_Menu()
    choise = menu.GetChoise()
    if choise == 1:
        ulke = input("ulke araması için en az 3 parametre")
        parametre1 = input("başlangıç yılı")
        parametre2 = input("bitiş yılı")
        bulunan_ulkeler = []
        for afet in veri:
            for nameKey, nameValue in afet.items():
                if ulke.lower() in nameValue.lower():
                    bulunan_ulkeler.append(afet)

        for afet in bulunan_ulkeler:
            for nameKey, nameValue in afet.items():
                if nameKey == "year":
                    if nameValue <= parametre2 and nameValue >= parametre1:
                        print(afet)


    if choise == 2:
        parametre1 = input("başlangıç yılı: ")
        parametre2 = input("bitiş yılı: ")

        for afet in veri:
            for nameKey, nameValue in afet.items():
                if nameKey == "year":
                    if nameValue <= parametre2 and nameValue >= parametre1:
                        print(afet)

    if choise == 3:
        disaster_type = input("tip giriniz: ")
        for afet in veri:
            for nameKey, nameValue in afet.items():
                if nameKey == "disaster subtype":
                    if disaster_type.lower() in nameValue.lower():
                        print(afet)

    if choise == 4:
        kita = input("kıta giriniz: ")
        for afet in veri:
            for nameKey, nameValue in afet.items():
                if nameKey == "continent":
                    if kita.lower() in nameValue.lower():
                        print(afet)

    if choise == 5:
        print("çıkış yapılıyor")
        break

