import math

def run():

    x1 = float(raw_input("Voer de eerste X-coordinaat in: "))
    x2 = float(raw_input("Voer de tweede X-coordinaat in: "))
    x3 = float(raw_input("Voer de derde X-coordinaat in: "))
    y1 = float(raw_input("Voer de eerste Y-coordinaat in: "))
    y2 = float(raw_input("Voer de tweede Y-coordinaat in: "))
    y3 = float(raw_input("Voer de derde Y-coordinaat in: "))

    u = (((x3 - x1)*(x2-x1))+((y3-y1)*(y2-y1)))/(((x2-x1)**2)+((y2-y1)**2))
    xv = x1 + (u * (x2 - x1))
    yv = y1 + (u * (y2 - y1))

    a = math.sqrt(((xv - x3)**2)+(yv - y3)**2)

    zone = ""

    print 
    if a >= 0 and a <= 12:
        zone = "territoriale wateren"
    elif a > 12 and a <= 24:
        zone = "aansluitende zone"
    elif a > 24 and a <= 200:
        zone = "exclusieve economische zone"
    elif a > 200:
        zone = "internationale wateren"

    print "voetpunt: (" + str(xv) + ", " + str(yv) + ")"
    print "afstand: " + str(a)
    print "zone: " + zone

run()