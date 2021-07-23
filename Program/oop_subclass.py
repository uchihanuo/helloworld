class SchoolMember:
    """Represent any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized School Member: {})'.format(self.name))

    def tell(self):
        """Tell my details."""
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    """Represent a teacher."""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    """Represent a student."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Dr.anyone', 50, 100000)
s = Student('Sherlock', 29, 99)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teacher and Students
    member.tell()
