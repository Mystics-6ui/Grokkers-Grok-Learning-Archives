pet = input('What animal would you like? ')
number = int(input('How many? '))
if pet.isupper() == True:
  print("Woah! No need to shout, you'll scare the animals!")
else:
  if number < 1:
    print("That's sad. No pet for you today.")
  elif number == 1:
    print("Great, here's your", pet + "!")
  elif number > 1:
    print("Ok!", number, pet + "s coming right up!")
