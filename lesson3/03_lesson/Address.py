class Address:

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return (f"{self.index}, {self.city}, {self.street}, {self.house},"
                f" Apt: {self.apartment}")


address = Address("101100", "Белореченск", "Ленина", "5", "8")
print(address)
