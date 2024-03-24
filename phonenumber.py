# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 08:28:34 2023

@author: Pranjal Arote
"""
import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+918796951245")
print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1,"en"));



import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+917756047085")
print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1,"en"));



from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter PhoneNumber:")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(reg)