start = int(input('Times table: '))
step = int(input('Step: '))

for n in range(3, 13, step):
  a = (start * n)
  print(f'{start} x [ ] = {a}')
