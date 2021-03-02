if number > 10000:
    traits = traits + 'excessive '
  if '3' in str(number):
    traits = traits + 'irksome '
  if number in arrogant_numbers:
    traits = traits + 'arrogant '
  return traits
# Write the rest of your program after this
count_dull_numbers = 0
numbers = input('Enter numbers: ')
numbers = numbers.split()
for number in numbers:
  desc = find_personality(int(number))
  if desc != '':
    print(f"{number} is an {desc}number.")
  else:
    count_dull_numbers = count_dull_numbers + 1
    
print(f"Dull numbers: {count_dull_numbers}")
