from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="geoapiExercises")


latitude = '30.8615936'
longitude = '29.5919441'


location = geolocator.reverse(latitude+","+longitude)


address = location.raw['address']


city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')


print('City : ', city)
print('State : ', state)
print('Country : ', country)
print('Zip Code : ', zipcode)
