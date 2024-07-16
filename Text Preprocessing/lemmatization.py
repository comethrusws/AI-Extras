from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('wordnet')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()
text = "better best running"
tokens = word_tokenize(text)
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
print(lemmatized_tokens)
