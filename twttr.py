word = input("Tweet ")
new_string = ''
for i in range(len(word)):
    letter = word[i]
    if letter == 'a'or letter == 'e' or letter == 'i' or letter == 'o' or letter =='u':
        pass
    else:
        new_string = new_string + letter
print(new_string)
