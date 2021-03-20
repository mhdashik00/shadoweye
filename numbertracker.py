import trunofficial

print('tool coded by mhdashik00')

phone = input('enter target phone number:')

owner = trunofficial.search(phone)

print(owner.name)

mobile = owner.phone
print(mobile.number)
print(mobile.countrycode)
print(mobile.carrier)


house = owner.address
print(house.city)
print(house.timezone)