text = "This    is an example   sentence with    extra spaces,  that should         theoretically, be    removed!"
text_without_extra_whitespace = ' '.join(text.split())
print(text_without_extra_whitespace)
