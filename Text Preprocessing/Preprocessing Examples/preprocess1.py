import nltk
import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    #lowercasing
    text = text.lower()
    #removing Punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    #wemoving Numbers
    text = re.sub(r'\d+', '', text)
    #tokenization
    tokens = word_tokenize(text)
    #removing Stop Words
    tokens = [word for word in tokens if word not in stop_words]
    #lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

text = "This is an example sentence, with numbers like 69696969, to demonstrate full preprocessing!"
processed_text = preprocess(text)
print(processed_text)
