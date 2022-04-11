def listToGcode(list):
    f = open("heartbeat.gcode", "w")

    for i in range(len(list[0])):
        x = str(list[0][i])
        y = str(list[1][i])
        f.write("G1 X" + x + " Y"+ y + " ;\n")
    f.close()