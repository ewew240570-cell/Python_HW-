from address import Address
from mailing import Mailing
from_address = Address(
    index="101000",
    city="Москва",
    street="ул. Тверская",
    house="12",
    apartment="34"
)
to_address = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="56",
    apartment="78"
)
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track="RU123456789"
)
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
