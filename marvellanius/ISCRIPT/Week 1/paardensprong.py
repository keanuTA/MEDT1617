def run():
    pos_now = raw_input("Startpositie: ")
    pos_goal = raw_input("Doelpositie: ")

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    string_now = pos_now[0]
    number_now = int(pos_now[1])

    string_goal = pos_goal[0]
    number_goal = int(pos_goal[1])

    string_number_now = alphabet.index(string_now)+1
    string_number_goal = alphabet.index(string_goal)+1

    diffletter = abs(string_number_goal - string_number_now)
    diffnumber = abs(number_now - number_goal)

    if (number_goal <= 8 and number_now <= 8 and string_number_now <= 8 and string_number_goal <= 8):
        if ((diffletter == 1 and diffnumber == 2) or (diffletter == 2 and diffnumber == 1)):
            print "Het paard kan springen van %s naar %s" %(pos_now,pos_goal)
        else:
            print "Het paard kan niet springen van %s naar %s" %(pos_now,pos_goal)
    else:
        print "Voer alstublieft correcte coordinaten in"

run()
