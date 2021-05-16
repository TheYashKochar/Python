# Program to get details from TrueCaller
from trunofficial import trunofficial
num  = input('Please Enter the Number : ')
owner = trunofficial.search('num')
mobile = owner.phone
print(mobile.number)
print(mobile.countrycode)
print(mobile.carrier)

house = owner.address
print(house.city)
print(house.timezone)
