class Smartphone:

    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        return (f"Smartphone(Brand: {self.brand},"
                f" Model: {self.model}, Phone Number: {self.phone_number})")


smartphone = Smartphone("Apple", "iphont 13", "+79000679559")
print(smartphone)
