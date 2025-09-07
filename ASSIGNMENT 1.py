# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Inherited class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Call parent constructor
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
phone2.make_call("+254700911507")
