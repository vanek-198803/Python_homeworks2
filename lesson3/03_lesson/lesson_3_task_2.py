class Smartphone:

    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.brand}, - {self.model}. {self.phone_number}"



catalog = [
    Smartphone("Apple", "iPhone 13", "+79001234567"),
    Smartphone("Samsung", "Galaxy S21", "+79007654321"),
    Smartphone("Xiaomi", "Mi 11", "+79009876543"),
    Smartphone("Google", "Pixel 6", "+79005432167"),
    Smartphone("OnePlus", "OnePlus 9", "+79004321654"),
]

for smartphone in catalog:
    print(smartphone)
