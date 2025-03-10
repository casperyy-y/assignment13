class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}, Salary: ${self.salary:,.2f}"

    def compute_bonus(self, rate):
        return self.salary * rate  

employee1 = Employee("John Doe", 60000)
print(employee1.display_info())

bonus_rate = float(input("Enter bonus rate (as decimal): ")) 
bonus = employee1.compute_bonus(bonus_rate)
print(f"Bonus: ${bonus:,.2f}")
