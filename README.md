# 🏗️ Object-Oriented Programming Assignment

## Assignment 1: Design Your Own Class! 📱

In this part of the assignment, we create a class to represent a **Smartphone**.  
The Smartphone inherits from a base class called `Device`.  

### Features Implemented:
- **Attributes**: brand, model, OS, storage, installed_apps  
- **Methods**: `install_app()`, `make_call()`, `phone_info()`  
- **Constructor**: Initializes each smartphone with unique values  
- **Inheritance**: `Smartphone` inherits from `Device`  

### Example Code:
```python
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
        self.installed_apps = []
    
    def install_app(self, app_name):
        self.installed_apps.append(app_name)
        print(f"{app_name} has been installed on {self.device_info()} 📱")
    
    def make_call(self, number):
        print(f"Calling {number} from {self.device_info()}... 📞")
    
    def phone_info(self):
        return f"{self.device_info()} runs {self.os} with {self.storage}GB storage."

# Example usage
phone1 = Smartphone("Samsung", "Galaxy A12", "Android", 128)
phone2 = Smartphone("Apple", "iPhone 14", "iOS", 256)

print(phone1.phone_info())
phone1.install_app("WhatsApp")
phone2.make_call("+254700123456")
```

---

## Activity 2: Polymorphism Challenge 🎭

We implement **vehicles** with a shared action `move()`.  
Each vehicle overrides `move()` differently, demonstrating **polymorphism**.

### Example Code:
```python
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
```

### Key Concepts Demonstrated:
- **Polymorphism**: Same method (`move()`) behaves differently in each class.  
- **Encapsulation**: Each class hides its unique implementation.  
- **Inheritance**: All vehicles derive from a common `Vehicle` class.  

---

## ✅ Learning Outcomes
By completing this assignment, you have practiced:
1. Designing your own classes with attributes and methods.  
2. Using constructors to initialize unique values.  
3. Implementing **inheritance** for code reusability.  
4. Exploring **polymorphism** with shared methods across classes.  
5. Demonstrating **encapsulation** by hiding internal implementations.  

---

💡 This assignment provides a solid foundation for mastering Object-Oriented Programming in Python.
