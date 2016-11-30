def run():
    age = int(raw_input("Voer uw leeftijd in (maanden): "))
    chlorid = int(raw_input("Voer uw chlorideconcentratie in (mmol/L): "))


    onwaarschijnlijk = "CF is hoogst onwaarschijnlijk"
    mogelijk = "CF is mogelijk"
    waarschijnlijk = "CF is waarschijnlijk"

    print age
    if(age <= 6):
        if(chlorid <= 29):
            print onwaarschijnlijk
        elif(chlorid >= 30 and chlorid <= 59):
            print mogelijk
        elif(chlorid >= 60):
            print waarschijnlijk
    elif(age > 6):
        if (chlorid <= 39):
            print onwaarschijnlijk
        elif (chlorid >= 40 and chlorid <= 59):
            print mogelijk
        elif (chlorid >= 60):
            print waarschijnlijk

run()