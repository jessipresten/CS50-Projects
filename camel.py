#ask for user input
word = input("Camel case ")
new_word = ''
for i in range(len(word)):
   letter = word[i]
   if letter.isupper():
       new_word = new_word + '_' + letter.lower()
   else:
       new_word = new_word + letter
print(new_word)
#convert camel case to snake case
#return
