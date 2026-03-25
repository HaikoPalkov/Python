# 03.12 Haiko Palkov
# Ülesanne 07

mootmine = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]

print(f"Mõõdetav kuu: {mootmine[0]}")
print(f"Viimane mõõtmine: {mootmine[-1]}")
print(f"Mõõdetav kuu: {mootmine[1:]}")

print(f"Suurim temperatuur: {max(mootmine[1:])}")
print(f"Vähim temperatuur: {min(mootmine[1:])}")
print(f"Keskmine: {sum(mootmine[1:])/sum(mootmine[1:]):.2f}")

print(f"-20 esineb: {mootmine[1:].count(-20)} korda")
# album = ['1. ALIKA – "Bridges"',
#         '2. Anett x Fredi – "Read Between The Lines"',
#         '3. villemdrillem – "leekiv armastus"',
#         '4. Clicherik & Mäx – "PAKSUD"',
#         '5. nublu – "ära ärata"',
#         '6. NOËP – "Move Your Feet"',
#         '7. Trad.Attack! – "Bring It On"',
#         '8. Bedwetters – "It Is What It Is"',
#         '9. Reket – "Panama paberid"',
#         '10. Grete Paia – "Võluväel"',]
# 
# print(album)
# valik = int(input("Vali lugu: "))
# print(album[valik-1])
