import random
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os
import nltk

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Expanded sample words array
sample_words = [
    "i","am","the","is","in","there","on","where","are","for","lol"
    "apple", "banana", "cat", "dog", "house", "computer", "program", 
    "learn", "play", "write", "eat", "run", "jump", "sleep", "happy", 
    "sad", "love", "hate", "good", "bad", "big", "small", "red", "blue", 
    "green", "yellow", "beautiful", "ugly", "fast", "slow", "new", "old", 
    "young", "rich", "poor", "man", "woman", "child", "student", "teacher", 
    "doctor", "engineer", "artist", "musician", "writer", "athlete", 
    "restaurant", "library", "park", "beach", "city", "country", "world", 
    "universe", "sun", "moon", "star", "planet", "tree", "flower", "river", 
    "mountain", "ocean", "sky", "cloud", "rain", "snow", "wind", "fire", 
    "earth", "life", "death", "time", "history", "future", "past", "present", 
    "idea", "dream", "goal", "success", "failure", "hope", "fear", "faith", 
    "belief", "science", "technology", "art", "culture", "music", "literature", 
    "film", "sport", "game", "friend", "family", "love", "hate", "peace", "war", 
    "freedom", "justice", "equality", "democracy", "government", "economy", 
    "industry", "business", "education", "health", "environment", "society", 
    "politics", "religion", "spirituality", "philosophy", "language", "communication", 
    "information", "knowledge", "wisdom", "truth", "fiction", "reality", "imagination", 
    "creativity", "passion", "emotion", "feeling", "expression", "experience", "journey", 
    "adventure", "challenge", "problem", "solution", "question", "answer", "cause", "effect", 
    "change", "progress", "development", "innovation", "discovery", "exploration", "discovery",
    "achievement", "celebration", "ceremony", "holiday", "tradition", "custom", "ritual", 
    "ceremony", "event", "occasion", "celebration", "festival", "birthday", "anniversary", 
    "wedding", "marriage", "divorce", "separation", "union", "bond", "relationship", "friendship", 
    "partnership", "alliance", "team", "group", "community", "society", "population", "nation", 
    "country", "state", "region", "continent", "world", "universe", "cosmos"
]

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return stemmed_tokens

def generate_meaningful_sentences(num_sentences):
    sentences = []
    for _ in range(num_sentences):
        sentence_length = random.randint(5, 15)
        sentence = ' '.join(random.choices(sample_words, k=sentence_length))
        sentences.append(sentence.capitalize() + '.')
    return sentences

num_sentences = 5
meaningful_sentences = generate_meaningful_sentences(num_sentences)

#directory to save the preprocessed files
output_dir = './Text Preprocessing/Preprocessing Examples/preprocessed_docs/meaningful'
os.makedirs(output_dir, exist_ok=True)

for idx, sentence in enumerate(meaningful_sentences):
    preprocessed_text = preprocess_text(sentence)
    preprocessed_text_str = ' '.join(preprocessed_text)
    output_file = os.path.join(output_dir, f"sentence_{idx + 1}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(preprocessed_text_str)
    print(f"Preprocessed Sentence {idx + 1} saved to {output_file}")

print("All sentences preprocessed and saved successfully.")
