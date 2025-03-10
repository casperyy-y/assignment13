class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}, Salary: ${self.salary:,.2f}"

class Manager(Employee):
    def long_term_bonus(self):
        return self.salary * 0.40  # 40% of salary as bonus

    def display_info(self):
        return f"Manager: {self.name}, Salary: ${self.salary:,.2f}, Long-term Bonus: ${self.long_term_bonus():,.2f}"

manager1 = Manager("Alice Johnson", 80000)
print(manager1.display_info())
