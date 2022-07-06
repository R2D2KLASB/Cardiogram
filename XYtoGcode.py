def listToGcode(list):
    # Create a new file
    f = open("heartbeat.gcode", "w")

    # From the given lists with results from the hearbeat sensor, Create useable gcode for the robot
    for i in range(len(list[0])):
        x = str(list[0][i])
        y = str(list[1][i])
        f.write("G1 X" + x + " Y"+ y + " ;\n")
    f.close()
