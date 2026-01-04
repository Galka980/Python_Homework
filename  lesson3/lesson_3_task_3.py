from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("658512", "Барнаул", "Крупской", "145", "15")
from_address = Address("658510", "Кемерово", "Волошиной", "33", "7")

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=1500,
    track="TRACK123654987"
)

# Распечатываем отправление в заданном формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")