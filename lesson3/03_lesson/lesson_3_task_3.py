from Address import Address
from Mailing import Mailing

to_address = Address("101100", "Белореченск", "Ленина", "5", "8")
from_address = Address("456206", "Златоуст", "Румянцева", "4", "25")

mailing = Mailing(to_address, from_address, 100.50, "TRACK2885")

track = mailing.track
from_index = mailing.from_address.index
from_city = mailing.from_address.city
from_street = mailing.from_address.street
from_house = mailing.from_address.house
from_apartment = mailing.from_address.apartment

to_index = mailing.to_address.index
to_city = mailing.to_address.city
to_street = mailing.to_address.street
to_house = mailing.to_address.house
to_apartment = mailing.to_address.apartment

cost = mailing.cost


print(f"Отправление {track} из {from_index}, {from_city}, {from_street}, {from_house} - {from_apartment} "
      f"в {to_index}, {to_city}, {to_street}, {to_house} - {to_apartment}. Стоимость {cost} рублей.")

