class Student:
    name: str
    age: int
    grades: []

    def __init__(self, name: str, age: int, grades: []):
        self.name: str = name
        self.age: int = age
        self.grades: [] = grades

    def add_grade(self, grade: int):
        self.grades.append(grade)
        return self.grades

    def average_grade(self):
       promedio = 0
        for i in range(len(self.grades)):
            cantidad = 0
            promedio = promedio + self.grades[cantidad]
            cantidad = cantidad + 1


