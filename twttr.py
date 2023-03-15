text = input("input: ")

# remove all vowels from the text
text_without_vowels = ""
for char in text:
    if char.lower() not in "aeiou":
        text_without_vowels += char

print("output:", text_without_vowels)
