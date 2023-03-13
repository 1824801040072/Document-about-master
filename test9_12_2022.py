class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return " xin chào Tôi là " + self.name + ". Trung năm nay, tôi được " + str(self.age) + " tuổi."


name = input("Nhập tên: ")
age = int(input("Nhập tuổi: "))
person = Person(name, age)
print(person.greeting())
