# Copy the code beneath the 'Write the rest of the program here' text.
# Put the print command inside the definition to avoid an error.

#  ________  _________  ________  ________        ________  ___  ___  _______   ________  _________  ___  ________   ________     
# |\   ____\|\___   ___\\   __  \|\   __  \      |\   ____\|\  \|\  \|\  ___ \ |\   __  \|\___   ___\\  \|\   ___  \|\   ____\    
# \ \  \___|\|___ \  \_\ \  \|\  \ \  \|\  \     \ \  \___|\ \  \\\  \ \   __/|\ \  \|\  \|___ \  \_\ \  \ \  \\ \  \ \  \___|    
#  \ \_____  \   \ \  \ \ \  \\\  \ \   ____\     \ \  \    \ \   __  \ \  \_|/_\ \   __  \   \ \  \ \ \  \ \  \\ \  \ \  \  ___  
#   \|____|\  \   \ \  \ \ \  \\\  \ \  \___|      \ \  \____\ \  \ \  \ \  \_|\ \ \  \ \  \   \ \  \ \ \  \ \  \\ \  \ \  \|\  \ 
#     ____\_\  \   \ \__\ \ \_______\ \__\          \ \_______\ \__\ \__\ \_______\ \__\ \__\   \ \__\ \ \__\ \__\\ \__\ \_______\
#    |\_________\   \|__|  \|_______|\|__|           \|_______|\|__|\|__|\|_______|\|__|\|__|    \|__|  \|__|\|__| \|__|\|_______|
#    \|_________|                                                                                                                 

#  |
#  |
#  |
# o o


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

