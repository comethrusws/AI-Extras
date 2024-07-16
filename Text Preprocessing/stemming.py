import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')

ps = PorterStemmer()
# Example text
text = "jack harlow's jordans look like jimmy neutron's forehead."
tokens = word_tokenize(text)
stemmed_tokens = [ps.stem(word) for word in tokens]
print(stemmed_tokens)
