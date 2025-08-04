class Day:
    def __init__(self, date):
        self.date = date
        self.schedule = {}

    def add_class(self, subject, teacher, students):
        self.schedule[subject] = {'teacher': teacher, 'students': students}