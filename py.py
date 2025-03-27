class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

def main():
    # Create a new student
    student = Student("John Doe", 20)
    
    # Add some grades
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(88)
    
    # Print student information
    print(f"Student Name: {student.name}")
    print(f"Student Age: {student.age}")
    print(f"Average Grade: {student.get_average():.2f}")

if __name__ == "__main__":
    main()
