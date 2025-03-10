class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()  
        self.credits = credits

    def compute_tuition(self):
        rate = 250 if self.district_code == "I" else 500
        return self.credits * rate

    def display_info(self):
        tuition = self.compute_tuition()
        return f"Student: {self.first_name} {self.last_name}, District: {self.district_code}, Credits: {self.credits}, Tuition Owed: ${tuition:,.2f}"
first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
district_code = input("Enter district code (I/O): ")
credits = int(input("Enter enrolled credits: "))

student1 = Student(first_name, last_name, district_code, credits)
print(student1.display_info())
