#'Python Community' -> #PythonCommunity
#'i like python community!' -> #ILikePythonCommunity
#'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string
punctuation = string.punctuation + " "
user_input = input("Insert your text : ")

user_input = user_input.title()

replacing = ""
for _ in user_input:
    if _ not in punctuation:
        replacing += _

if len(replacing) > 140:
    replacing = replacing[:140]

print("Your hashtag:")
print("#"+replacing)
