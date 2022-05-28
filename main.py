

class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        print ("Name: " + self.name)
    def change_age(self, new_age):
        self.age = new_age
        print ("Age: " + str(self.age))
    def add_track(self, new_track):
        self.tracks.append(new_track)
        print("Tracks:")
        for track in self.tracks:
            print ("\t" + track)
    def change_score(self, new_score):
        self.score = new_score
        print("Score: " + str(new_score))

Bob = Student(name="Bob", age="26", tracks=["UI/UX"], score=20.90)

Bob.change_name("Emma")
Bob.change_age(23)
Bob.add_track("Backend-Djano")
Bob.change_score(50.3)
