#Pizza Siparişi
"""
Küçük boy (S) pizza:40 TL
Orta boy (M) pizza: 50 TL
Büyük boy (L) pizza: 60 TL

Ekstra peynirin pizza boyutlarına göre fiyatlandırılması:
Küçük boy (S) pizzaya +5TL
Orta boy (M) ve büyük boy (L) pizzaya + 10 TL

İçecek istiyorsa +20 TL
"""


print("PYTHON PİZZA'YA HOŞGELDİNİZ!")
boyut=input("Pizza boyutunuz nasıl olsun?(S/M/L):")
ekstra_peynir=input("Ekstra peynir ister misiniz?(E/H):")
icecek=input("İçecek ister misiniz?:")

if(boyut=="S"):
    if(ekstra_peynir=="E"):
        if(icecek=="E"):
            print("Tutar:",40+5+20)
        else:
            print("Tutar:", 40 + 5)
    else:
        if (icecek == "E"):
            print("Tutar:", 40 +20)
        else:
            print("Tutar:", 40)


elif(boyut=="M"):
    if(ekstra_peynir=="E"):
        if(icecek=="E"):
            print("Tutar:",50+10+20)
        else:
            print("Tutar:", 50 + 10)
    else:
        if (icecek == "E"):
            print("Tutar:", 50 +20)
        else:
            print("Tutar:", 50)

else:
    if(ekstra_peynir=="E"):
        if(icecek=="E"):
            print("Tutar:",60+10+20)
        else:
            print("Tutar:", 60 + 10)
    else:
        if (icecek == "E"):
            print("Tutar:", 60 +20)
        else:
            print("Tutar:", 60)