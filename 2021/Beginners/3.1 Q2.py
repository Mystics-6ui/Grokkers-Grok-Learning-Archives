x = int(input('Wind speed? '))
if x < 10:
  print('No flying today.')
elif x > 40:
  print('Dangerous wind conditions!')
else:
  print('Perfect kite weather!')
