# 03.12 Haiko Palkov
# Ülesanne 06
import math
import turtle

turtle.speed(0)
mootkava = 50

nurk = math.radians(53)
korgus = 4.4

kaugus = korgus / math.tan(nurk)
pikkus = round(math.sqrt(math.pow(korgus,2) + math.pow(kaugus,2)),2)

print(pikkus)
print(kaugus)
print(nurk)

turtle.fd(kaugus * mootkava)
turtle.lt(90)
turtle.fd(korgus * mootkava)
turtle.lt(143)
turtle.fd(pikkus * mootkava)

turtle.done()