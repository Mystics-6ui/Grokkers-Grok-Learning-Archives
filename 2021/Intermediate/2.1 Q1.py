country = input('Country: ')
if country in tour_locations:
  print(f'{country} is on the list!')
else:
  print(f'We will not be in {country} this time.')
