#trying ouy preprocessing with spacy

import spacy

nlp = spacy.load('en_core_web_sm')

text = "Let's See how This Works out man, idk. We'll see. it is what it is, 3am bhayo. sut abo"

doc = nlp(text)
processed_tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
print(processed_tokens)
