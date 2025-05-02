import emoji

#ask for user input in English
user_answer = input("Input: ")

output = emoji.emojize(user_answer, language = 'alias')
print("Output:",  output)








