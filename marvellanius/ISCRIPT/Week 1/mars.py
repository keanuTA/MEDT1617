def run():
    invoer = raw_input("How many sol?")
    sol = int(invoer)

    # Aantal aardse seconden in een sol
    sol_seconden = 88775.244

    # Total number of seconds on the amount of sol in input
    seconden = sol * sol_seconden

    # Floor divide seconds in days
    dagen = seconden // 86400
    seconden -= 86400*dagen

    # Floor divide rest of seconds in hours
    uren = seconden // 3600
    seconden -= 3600*uren

    # And then floor divide the rest of the seconds into minutes
    minuten = seconden // 60
    seconden -= 60*minuten

    # First convert all floats to ints, then to strings, then print them.
    print(str(sol) + " sol = " + str(int(dagen)) + " dagen, " + str(int(uren))+ " uren, " + str(int(minuten)) + " minuten en " + str(int(seconden)) + " seconden.")

run()
