Message = input('Message: ')
if 'caramel' in Message :
  mess = Message.replace('caramel', 'SECRET')
  print(mess)
else:
  print('Nothing is secret.')
