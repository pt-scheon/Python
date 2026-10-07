import csv
files=[["tri.py"],["tris1o.py"],["robot.py"],["circle.py"]]
with open("commands2.csv","w") as g:
    write=csv.writer(g)
    write.writerows(files)
    
filename=input("")

with open("commands2.csv") as f:
    read=csv.reader(f)
    for row in read:
        if row:
            if filename=="tri.py":
                import auv.shapes.triangle as triangle
            elif filename=="tris1o.py":
                import auv.shapes.parallelogram as parallelogram
            elif filename=="robot.py":
                import auv.shapes.robot as robot
            elif filename=="circle.py":
                import auv.shapes.fancycircle as fancycircle
