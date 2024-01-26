
try:
    print("Tere! Olen sinu uus sõber - Python!")
    nimi=input("Mis on sinu nimi?")
    print(nimi, ", oi kui ilus nimi!")
    yesno=int(input("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if yesno==1:
        pikkus=int(input("Sisesta oma pikkus: "))
        mass=int(input("Sisesta oma kaal: "))
        indeks=mass / (0.01 * pikkus) ** 2
        print (nimi + "! Sinu keha indeks on:", round(indeks,1))
        if indeks<16:
            print("Tervisele ohtlik alakaal")
        elif 16<indeks<=19:
            print("Alakaal")
        elif 19<indeks<=25:
            print("Normaalkaal")
        elif 25<indeks<=30:
            print("Ülekaal")
        elif 30<indeks<=35:
            print("Rasvumine")
        elif 35<indeks<=40:
            print("Tugev rasvumine")
        else:
            print("Tervisele ohtlik rasvumine")

    else:
        print("Kahju! See on väga kasulik info!")
        print()

        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

except ValueError:
    print("Viga! Palun sisesta õiged numbrid.")