band = input('Band: ')
song = input('Songs: ')
OHNO_list = song.split()
print(f'Please welcome to the stage, {band}!')
print('They will be playing...')
for item in OHNO_list:
  print(f'🎵 {item}')
print(f'Give it up for {band}!')
