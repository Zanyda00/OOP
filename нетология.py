class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self):
        average = sum(sum(i) for i in self.grades.values()) / sum(len(i) for i in self.grades.values())
        return round(average, 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}' \
               f'\nСредняя оценка за домашние задания: {self._average_rating()}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self._average_rating() < other._average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def _average_rating(self):
        average = sum(sum(i) for i in self.grades.values()) / sum(len(i) for i in self.grades.values())
        return round(average, 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_rating()}'

    def __lt__(self, other):
        return self._average_rating() < other._average_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def average_rating_hw_for_course(student_list, course):
    average = sum(sum(student.grades[course]) for student in student_list if course in student.grades) /\
              sum(len(student.grades[course]) for student in student_list if course in student.grades)
    return round(average, 1)


def average_rating_lecturer_for_course(lecturer_list, course):
    average = sum(sum(lecturer.grades[course]) for lecturer in lecturer_list if course in lecturer.grades) /\
              sum(len(lecturer.grades[course]) for lecturer in lecturer_list if course in lecturer.grades)
    return round(average, 1)


student_1 = Student('Иван', 'Васильевич', 'муж.')
student_1.finished_courses += ['Условные операторы']
student_1.finished_courses += ['Циклы']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

student_2 = Student('Николай', 'Николаевич', 'муж.')
student_2.finished_courses += ['Циклы', 'Функции']
student_2.courses_in_progress += ['Python', 'Git', 'ООП']

lecturer_1 = Lecturer('Иосиф', 'Иосифович')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Моисей', 'Моисеевич')
lecturer_2.courses_attached += ['Python', 'ООП']

reviewer_1 = Reviewer('Евгений', 'Анатольевич')
reviewer_1.courses_attached += ['Python', 'Git', 'ООП']

reviewer_2 = Reviewer('Иван', 'Иванов')
reviewer_2.courses_attached += ['Python', 'Git', 'ООП']


reviewer_1.rate_hw(student_1, 'Python', 1)
reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Python', 4)

reviewer_1.rate_hw(student_1, 'Git', 5)
reviewer_1.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 8)

student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 6)
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Git', 10)
student_1.rate_lecture(lecturer_1, 'Git', 6)
student_1.rate_lecture(lecturer_1, 'Git', 10)
student_2.rate_lecture(lecturer_2, 'Python', 1)
student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Python', 3)
student_2.rate_lecture(lecturer_2, 'ООП', 7)
student_2.rate_lecture(lecturer_2, 'ООП', 9)
student_2.rate_lecture(lecturer_2, 'ООП', 5)

print(student_1)
print()
print(lecturer_1)
print()
print(reviewer_1)
print()
print(student_1 < student_2)
print()
print(lecturer_1 > lecturer_2)
print()

print(average_rating_hw_for_course(Student.student_list, 'Python'))
print(average_rating_hw_for_course(Student.student_list, 'Git'))

print()

print(average_rating_lecturer_for_course(Lecturer.lecturer_list, 'Python'))
print(average_rating_lecturer_for_course(Lecturer.lecturer_list, 'Git'))
print(average_rating_lecturer_for_course(Lecturer.lecturer_list, 'ООП'))
