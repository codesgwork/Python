class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
  def display(self):
    print(self.name)
    print(self.age)
human1 = Human("John", 22)
human1.display()
human2 = Human("Alice", 23)
human2.display()
human3 = Human("Bob", 24)
human3.display()
# Class Variable
class Human:
  population = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age
    Human.population += 1
  def display(self):
    print(self.name)
    print(self.age)
    print(Human.population)
human1 = Human("John", 22)
human1.display()
human2 = Human("Alice", 23)
human2.display()
human3 = Human("Bob", 24)
human3.display()
# Inheritance
class Parent:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name)
    print(self.age)
class Child(Parent):
  def __init__(self, name, age, grade):
    Parent.__init__(self, name, age)
    self.grade = grade
  def display(self):
    Parent.display(self)
    print(self.grade)
child1 = Child("John", 22, "A")
child1.display()
child2 = Child("Alice", 23, "B")
child2.display()
child3 = Child("Bob", 24, "C")
child3.display()
# Multiple Inheritance
class Parent1:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name)
    print(self.age)
class Parent2:
  def __init__(self, grade):
    self.grade = grade
  def display(self):
    print(self.grade)
class Child(Parent1, Parent2):
  def __init__(self, name, age, grade):
    Parent1.__init__(self, name, age)
    Parent2.__init__(self, grade)
  def display(self):
    Parent1.display(self)
    Parent2.display(self)
child1 = Child("John", 22, "A")
child1.display()
child2 = Child("Alice", 23, "B")
child2.display()
child3 = Child("Bob", 24, "C")
child3.display()
# Multilevel Inheritance
class GrandParent:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name)
    print(self.age)
class Parent(GrandParent):
  def __init__(self, name, age, grade):
    GrandParent.__init__(self, name, age)
    self.grade = grade
  def display(self):
    GrandParent.display(self)
    print(self.grade)
class Child(Parent):
  def __init__(self, name, age, grade, school):
    Parent.__init__(self, name, age, grade)
    self.school = school
  def display(self):
    Parent.display(self)
    print(self.school)
child1 = Child("John", 22, "A", "XYZ")
child1.display()
child2 = Child("Alice", 23, "B", "ABC")
child2.display()
child3 = Child("Bob", 24, "C", "DEF")
child3.display()
# super() Function
class GrandParent:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name)
    print(self.age)
class Parent(GrandParent):
  def __init__(self, name, age, grade):
    super().__init__(name, age)
    self.grade = grade
  def display(self):
    super().display()
    print(self.grade)
class Child(Parent):
  def __init__(self, name, age, grade, school):
    super().__init__(name, age, grade)
    self.school = school
  def display(self):
    super().display()
    print(self.school)
child1 = Child("John", 22, "A", "XYZ")
child1.display()
child2 = Child("Alice", 23, "B", "ABC")
child2.display()
child3 = Child("Bob", 24, "C", "DEF")
child3.display()
# Polymorphism
# Inheritance
class Parent:
  def display(self):
    print("Parent")
class Child(Parent):
  def display(self):
    print("Child")
Family = [Parent(), Child()]
for member in Family:
  member.display()
# Duck Typing
class Parent:
  def display(self):
    print("Parent")
class Child:
  def display(self):
    print("Child")
Family = [Parent(), Child()]
for member in Family:
  member.display()
# @abstractmethod
from abc import ABC, abstractmethod
class Parent(ABC):
  @abstractmethod
  def display(self):
    pass
class Child(Parent):
  def display(self):
    print("Child")
Family = [Parent(), Child()]
for member in Family:
  member.display()
# @staticmethod
class Parent:
  @staticmethod
  def display():
    print("Parent")
class Child(Parent):
  @staticmethod
  def display():
    print("Child")
Family = [Parent(), Child()]
for member in Family:
  member.display()
# @classmethod
class Parent:
  @classmethod
  def display(cls):
    print("Parent")
class Child(Parent):
  @classmethod
  def display(cls):
    print("Child")
Family = [Parent(), Child()]
for member in Family:
  member.display()
# Magic Methods
# __init__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name)
    print(self.age)
human1 = Human("John", 22)
human1.display()
human2 = Human("Alice", 23)
human2.display()
human3 = Human("Bob", 24)
human3.display()
# __str__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return self.name + " " + str(self.age)
human1 = Human("John", 22)
print(human1)
human2 = Human("Alice", 23)
print(human2)
human3 = Human("Bob", 24)
print(human3)
# __add__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __add__(self, other):
    return self.age + other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 + human2)
# __sub__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __sub__(self, other):
    return self.age - other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 - human2)
# __mul__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __mul__(self, other):
    return self.age * other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 * human2)
# __truediv__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __truediv__(self, other):
    if other.age == 0:
      return "Division by Zero"
    return self.age / other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 / human2)
# __floordiv__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __floordiv__(self, other):
    if other.age == 0:
      return "Division by Zero"
    return self.age // other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 // human2)
# __mod__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __mod__(self, other):
    if other.age == 0:
      return "Division by Zero"
    return self.age % other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 % human2)
# __pow__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __pow__(self, other):
    return self.age ** other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 ** human2)
# __eq__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __eq__(self, other):
    return self.age == other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 == human2)
# __ne__()
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __ne__(self, other):
    return self.age != other.age
human1 = Human("John", 22)
human2 = Human("Alice", 23)
print(human1 != human2)
