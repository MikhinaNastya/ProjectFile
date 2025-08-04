from days import Day
from subjects import Subject
from grades import Grade
from students import Student
from teachers import Teacher


# Пример использования:

# Создание преподавателя и студента
teacher1 = Teacher("Шмигирилова Ирина Борисовна")
teacher2 = Teacher("Дуткин Матвей Александрович")
teacher3 = Teacher("Копнова Оксана Леонидовна")

student1 = Student("Волков Максим")
student2 = Student("Деткина Валерия")
student3 = Student("Ефимов Дмитрий")

student1.add_course("Образовательная Информатика")
student2.add_course("Образовательная Математика")
student3.add_course("Образовательная Информатика")


# Создание предмета и дня
math_subject = Subject("Высшая математика")
inform_subject = Subject("Прикладная информатика")
robot_subject = Subject("Робототехника")


day1 = Day("2024-01-22")
day2 = Day("2024-01-23")
day3 = Day("2024-01-24")
day4 = Day("2024-01-25")
day5 = Day("2024-01-26")


# Добавление студента и преподавателя в предмет
day1.add_class(math_subject, teacher1, [student2])
day2.add_class(inform_subject, teacher2, [student1])
day3.add_class(robot_subject, teacher3, [student3])

# Внесение оценки
math_grade = Grade(student2, math_subject, 90)
inform_grade = Grade(student1, inform_subject, 100)
robot_grade = Grade(student3, robot_subject, 95)
print()
# Вывод информации
print(f"{student2.name} посещает занятие по предмету {math_subject.name}, преподаватель {teacher1.name} в {day1.date}.")
print(f"Оценка по предмету {math_subject.name}: {math_grade.value}")
print()
print(f"{student1.name} посещает занятие по предмету {inform_subject.name}, преподаватель {teacher2.name} в {day2.date}.")
print(f"Оценка по предмету {inform_subject.name}: {inform_grade.value}")
print()
print(f"{student3.name} посещает занятие по предмету {robot_subject.name}, преподаватель {teacher3.name} в {day3.date}.")
print(f"Оценка по предмету {robot_subject.name}: {robot_grade.value}")


