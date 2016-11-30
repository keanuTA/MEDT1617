import math

def run():
    radial = float(raw_input("Please input the radial to convert: "))
    degrees = math.degrees(radial)

    minutes = (degrees%1)*60

    seconds = (minutes%1)*60

    print int(degrees)
    print int(minutes)
    print int(seconds)

run()