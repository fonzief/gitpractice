

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
#varfor type(grade) is Grade???? en typ ar riktad mot en klass???
    def get_avarage(self):
        self.avarage = ave/len(self.grades)
        ave = 0
        for n in self.grades:
            ave += n

##########hur printar jag avarage??

class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(100)
###varfor grade har igen???

print(pieter.__dict__)
##varfor ar grades tom??
print(pieter.get_avarage)

#
#<bound method Student.get_avarage of <__main__.Student instance at 0x102881f38>>
#vill ha siffror
