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
