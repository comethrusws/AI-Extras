import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = "Text Preprocessing Looks Fun. Percy's Panda Told Me to Worship Perceptron Neurons. I am A Lunatic."
tokens = word_tokenize(text)
print(tokens)
