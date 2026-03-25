# Haiko Palkov
# 18.11.25
# Harjutus 04

# Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
# Aed on ristküliku kujuline.
# Programm peaks küsima kasutajalt kahe aiaosa pikkused meetrites ja seejärel arvutama aia kogupikkuse.
# Väljasta lause, kasutades f-string vormindamist.
# Näide:
# Kasutaja sisestab: 4 ja 5
# Programm väljastab: Aia kogupikkus on 18 meetrit.

a = int(input("Anna külg 1: "))
b = int(input("Anna külg 2: "))
ymber = 2 * (a + b)

print(f"Aia kogupikkus on {ymber} meetri.")

# Faili allalaadimine
# 
#     Kirjuta programm, mis aitab arvutada, kui kaua kulub aega faili allalaadimiseks.
#     Programm küsib kasutajalt faili suurust megabaitides (MB) ja allalaadimiskiirust megabaitides sekundis (MB/s).
#     Seejärel arvutab programm allalaadimiseks kuluvat aega minutites.
#     Lisa kontroll, et programm ei jookseks kokku, kui kasutaja sisestab ebakorrektse allalaadimiskiiruse (nt null või negatiivne arv).
#     Väljasta lause, kasutades f-string vormindamist
#     Näide:
#     Kasutaja sisestab: faili suurus 500 MB, kiirus 20 MB/s
#     Programm väljastab: Allalaadimiseks kulub 25 sekundit.
#     Kui kasutaja sisestab kiiruseks 0 või teksti, siis programm ütleb: Tegid sisestamisel vea!
print(5//2)SSSS
try:
    suurus = int(input("faili suurust megabaitides (MB):"))
    kiirus = int(input("llalaadimiskiirust (MB/s): "))
    aeg = (suurus / kiirus) / 60
    print(f"Allalaadimiseks kulub {aeg:0.2f} minutit.") #f0.2 ümardab 2 komakohta
except:
    print("kle muna, vahi sisestust")