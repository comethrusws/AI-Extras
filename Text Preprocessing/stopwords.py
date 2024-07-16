import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# download stopwords
nltk.download('stopwords')
nltk.download('punkt') 

stop_words = set(stopwords.words('english'))

text = "no really, what the hell are stop words now? Preston's Pink Panda Propels Propane preaching the Purgatory."
tokens = word_tokenize(text)
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print(filtered_tokens)
