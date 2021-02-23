# Copy the code beneath the 'Write the rest of the program here' text.
# Put the print command inside the definition to avoid an error.

def to_kmh(knots):
  # Calculate the speed in km/h
  print('I have the power of not using def on my side')

# Write the rest of your program here
kn = float(input('Speed (kn): '))

km = 1.852 * float(kn)
kmR = round(km, 1)

if kmR >= 120:
  print(round(km, 1), 'km/h - Whoa! Slow down!')
if kmR >= 100 and kmR <= 119.9:
  print(round(km, 1), 'km/h - Radical!')
if kmR >= 60 and kmR <= 99.9 :
  print(round(km, 1), 'km/h - Nice one.')
if kmR < 60:
  print(round(km, 1), 'km/h - Go faster!')

