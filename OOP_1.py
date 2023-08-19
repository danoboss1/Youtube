class Person:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def greet(self):
        print(f"Hello, I'm {self.full_name()}!")

    def get_contact_info(self):
        contact_info = {
            "Full Name": self.full_name(),
            "Age": self.age,
            "Email": self.email
        }
        return contact_info

# Test the Person class
person1 = Person("John", "Doe", 30, "john@example.com")
print("Full Name:", person1.full_name())
person1.greet()
print("Contact Info:", person1.get_contact_info())