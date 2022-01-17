import math
import random
#A ariketa:Sarrera bezala emandako zenbaki negatibo baten balio absolutua kalkulatu
print("A ariketa")
x = -5
print(abs(x))

#B ariketa: Bi   zenbaki   oso   gehitu (edozein,   bi   aldagai   definituta   ematen   diezuen balioekin)
print("B ariketa")
x = 5
y = 6
print(y + x)

#C ariketa: Tenperaturen  bihurketa  bat  egin  Celsius  graduetatik (tCelsiussarrerabalio bezala hartuz) Fahrenheitgraduetara:
print("C ariketa")
celsius = 20
faren = 9/5 * celsius + 32
print(faren)

#D ariketa: Esfera baten azalera kalkulatu (erradioasarrera bezala pasata)
print("D ariketa")
erradio = 2
azalera =  4 * math.pi * erradio**2
print(azalera)

#E ariketa: a, b eta c aldagaietan gordetako 3 zenbaki emanda (a eta b-k balio berdina eta 
# c-k   balio   handiago   bat   edukita), ondorengoa   egiaztatzen   duten assertaginduak programatu
print("E ariketa")
a = 5
b = 5
c = 7

assert a == b
assert b < c
assert c > a

print("baldintza guztiak betetzen dira")

#F. ariketa: Bi   puntuen   arteko   distantzia   euklidearra kalkulatu. Sarrera   bezala   bi 
# puntuen  koordenatuak  eskatzen  dira. (x1,  y1),  (x2,  y2)bi  puntu  emanda,  bi puntuen
#  arteko distantzia kalkulatzen duen formula honakoada
print("F ariketa")
x1, y1 = 1,2
x2, y2 = 2,1

d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(d)

#G ariketa: Ondorengo adierazpena kalkulatu (x eta y sarrerako datuak dira):
print("G ariketa")
x = 1
y = 2
res = 5 * x**3 + math.sqrt(x**2+y**2) + math.e**math.log(x)
print(res)
#H ariketa: Ondorengo balioak dituen datu bildumabat sortu Python-en:1, 2, 3, 4, 5Kortxete eragileak  
# erabili ([,  ])bildumako  elementuen  hasiera  eta  bukaera adierazteko.
print("H ariketa")
bilduma = [1,2,3,4,5]
print(type(bilduma))

#I ariketa: Python-en  4  zenbakiaren  gutxienez  3  agerpen  dituen  zerrenda  bat  sortu.  4 zenbakiaren agerpen guztiak10 zenbakiaz ordezkatu.
print("I ariketa")
v = [4,3,4,2,3,4,1,2,3]

b = [10 if elem==4 else elem for elem in v]
print(b)

#J ariketa: Atera  pantaila  bidezemandako  zenbaki  zerrendako  zenbaki  guztiak  1era laburtzeko behar den 
# pausu kopurua. Zenbaki bat 1era murrizteko, zenbakia bikoitia bada 2tik zatitzen da, bakoitia den kasuan 
# zenbakia bider 3 gehi bat delarik. Zerrenda  bat  lortu  behar  da jatorrizko  zerrendako zenbaki bakoitza 
# 1era laburtzeko behar izan den pausu kopuruarekin.
print("J ariketa")

#funtzio honetan x zenbaki bat sartzerakoan, 1era laburtzen du
def batera_laburtu(x):
    k = 0
    
    while x != 1: #x bat ez den bitartean loop-ean egongo da
        if x%2==0:
            x/=2
        else:
            x = x*3+1
        k+=1
    return k

v = [6,11,27,32,33]
b = [batera_laburtu(elem) for elem in v]
print(b)

#K ariketa:-5 eta 5 arteko balioak (edozein) dituen 6x3 tamainako matrize bat sortu.
print("K ariketa")
v = [[random.randint(-5,5) for x in range(3)] for y in range(6)]
print(v)

#L ariketa: Python-en funtzio bat sortu sarrera bezala edozein dimentsioko matrize 
# bat eta  x  zenbaki  bat  hartuta,  x  zenbakia  matrize  horretan  azaltzen  den  aldi kopurua bueltatzen duena.

print("L ariketa")
v = [3,3,3,1,2,3,4]
def x_kop(m, x):
    return m.count(x)
print(x_kop(v, 3))
#M ariketa:Konputazio Eredu Abstraktuak1. Laborategia3de 3m)Sortu Python funtzio bat matrize 
# batean 4 eta 7 zenbakien artean (biak barne) dagoen zenbakiren bat egonda Truebueltatzen duena eta Falsebestela.
print("M ariketa")
v = [[1,2],[1,5],[3,7]]
def tartea(m):
    for v in m: #bi for auekin matrize soa iteratzen da
        for i in v:
            if i>=4 and i<=7:
                return True
    return False
print(tartea(v))
#N ariketa: Tamaina    berdina    duten    zenbaki    oso    zerrenda    bat    (bai    positibo    edo negatiboak)  eta  
# boolearren  zerrenda  (Trueedo Falsebalioak  dituena)  bat emanda,funtzio bat sortu posizio baliokideetan 
# zenbaki positibo bat Trueeta zenbaki negatibo bat Falseden aldi kopurua bueltatzen duena.
print("N ariketa")

v = [True, True, False, False]
w = [1, 1,-1,1]

def posizio_berdinak(bool_v, int_v):
    positiboa = 0
    negatiboa = 0
    for i in range(0,len(bool_v)):#bi listak iteratzen dira batera
        if bool_v[i]==True and int_v[i]>=0:
            positiboa += 1
        elif bool_v[i]==False and int_v[i] < 0:
            negatiboa += 1
    return positiboa, negatiboa

x, y = posizio_berdinak(v, w)
t = (x,y)
print(t)