import math

def run():

    input_x = float(raw_input("X coordinate: "))
    input_y = float(raw_input("Y coordinate: "))


    r = math.sqrt((math.pow(input_x,2) + math.pow(input_y,2))) # math.sqrt(input_x**2 + input_y**2)
    angle = math.atan2(input_y, input_x)

    print r
    print angle

run()