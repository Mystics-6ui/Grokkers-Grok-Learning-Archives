word_list = input('Sentence: ').split()
counter = 0
for word in word_list:
  if word.isupper() == True:
    counter = counter + 1

print(f'Number of shouted words: {counter}')
