import random
import math

valinta=int(input("tehtävä"))
"""
if valinta==0:
    print("-"*100)
    print("Joe")
    print("-"*100)



    print("-"*100)
    print("Meikä poika asuu kuninkaan linnassa", int(3))
    print("-"*100)
"""
if valinta==1:
    nimi=input("Mikä on sun nimi? :)")
    print("Moi",nimi)

elif valinta==2:
    sade=int(input("Säde?"))
    sade=sade**2*math.pi
    print("Ympyrän säde on",sade)

elif valinta==3:
    kanta=float(input("kanta?"))
    korkeus=float(input("korkeus?"))
    area=kanta*korkeus
    perimiter=kanta*2+korkeus*2

    print("pinta ala on", area, "ja piiri on", perimiter)

elif valinta==4:
    eka=int(input("eka?"))
    toka=int(input("toka?"))
    kolmas=int(input("kolmas?"))

    sum=eka+toka+kolmas
    product=eka*toka*kolmas
    mean=sum/3
    print("summa on",sum,"ja tulo on", product, "ja keskiarvo on", mean)

elif valinta==5:
    g=1
    kg=1000
    luoti=13.3*g
    naula=32*luoti
    leiviska=20*naula

    leiviskäInput=float(input("leiviskät?"))
    naulaInput=float(input("naulat?"))
    luotiInput=float(input("luodit?"))

    mass=leiviskäInput*leiviska+naulaInput*naula+luotiInput*luoti
    masskg=int(mass/1000)
    massg=mass-masskg*1000

    print("Massa nykymittojen mukaan on",masskg, "kiloa ja", massg,"grammaa" )

elif valinta==6:

    kol=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    nel=str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))
    print(kol,nel)
    #print(id(kol))

