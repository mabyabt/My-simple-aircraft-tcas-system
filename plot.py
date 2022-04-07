from this import d


class Airplane:
    attitude = 0
    heading = 0
    id=0


text_file = open("airplane_data.dat", "r")
lines = text_file.readlines()


self = Airplane()
self.attitude = 1000
self.heading = 180
self.id = 1

airplane2 = Airplane()
airplane2.attitude =  lines[0]
airplane2.heading = lines[1]
aLeinght = len(lines)
i=0
while aLeinght != i:

    airplane2.attitude.append(lines[i+2])
    airplane2.heading.append(lines[i+3])
    ++i






