import re

text = "2024 is a rollercoaster. i wanna go homeeeeeeeee"
text_without_numbers = re.sub(r'\d+', '', text)
print(text_without_numbers)
