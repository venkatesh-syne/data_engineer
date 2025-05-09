class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def name_details(self):
        return f'{self.firstname,self.lastname}'
    def other_details(self):
        return f'{self.age,self.country,self.city}'



details = Person('Venkat','M','30','India','Bengaluru')
print(type(details.other_details()))

