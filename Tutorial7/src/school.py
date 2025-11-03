class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self, years):
        self.age += years

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, uid):
        super().__init__(name, age)
        self.uid = uid

    def introduce(self):
        return f"{super().introduce()} My UID is {self.uid}."


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"{super().introduce()} I teach {self.subject}."


def main():
    alice = Student("Alice", 20, "S12345")
    bob = Teacher("Bob", 40, "Mathematics")

    print(alice.introduce())
    # Output: Hello, my name is Alice and I am 20 years old. My UID is S12345.

    print(bob.introduce())
    # Output: Hello, my name is Bob and I am 40 years old. I teach Mathematics.

    bob.aging(5)
    print(bob.introduce())
    # Output: Hello, my name is Bob and I am 45 years old. I teach Mathematics.


main()
