class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} добавлен на курс {course_name}")

    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{self.name} удален с курса {course_name}")
        else:
            print(f"{self.name} не был зарегистрирован на курсе {course_name}")

