class Emp:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print("calling init")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __str__(self):
        return f"Emp(name={self.name}, age={self.age}, salary={self.salary})"

    def __new__(cls, name, age, salary):
        print("Creating a new instance of Emp")
        return super(Emp, cls).__new__(cls)
