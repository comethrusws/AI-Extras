import string

text = "Johnnhy Bravo's Favorite Pants are a Poor Man's Prada."
text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
print(text_without_punctuation)
