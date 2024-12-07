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


class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Mailing from {self.from_address} to {self.to_address},"
                f"Cost: {self.cost}, Tracking Number: {self.track}")


to_address = Address("101100", "Белореченск", "Ленина", "5", "8")
from_address = Address("456206", "Златоуст", "Румянцева", "4", "25")
mailing = Mailing(to_address, from_address, 100.50, "TRACK2885")

print(Mailing)
