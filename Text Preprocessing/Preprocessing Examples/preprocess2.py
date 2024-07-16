import random
import string
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os

# download nltj resources if not already downloaded
import nltk
nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return stemmed_tokens

def generate_sample_data(num_documents):
    sample_data = []
    for _ in range(num_documents):
        text = "<html><body>"
        text += ' '.join(random.choices(string.ascii_letters + string.digits, k=random.randint(50, 200)))
        text += "</body></html>"
        sample_data.append(text)
    return sample_data

#generate 5 sample documents
sample_documents = generate_sample_data(10)

output_dir = './Text Preprocessing/Preprocessing Examples/preprocessed_docs'
os.makedirs(output_dir, exist_ok=True)
for idx, doc in enumerate(sample_documents):
    preprocessed_text = preprocess_text(doc)
    preprocessed_text_str = ' '.join(preprocessed_text)
    # Save to file
    output_file = os.path.join(output_dir, f"document_{idx + 1}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(preprocessed_text_str)
    print(f"Preprocessed Document {idx + 1} saved to {output_file}")

print("all documents preprocessed and saved successfully.")
