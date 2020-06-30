from pathlib import Path

path = Path(__file__).parent / "../raw/words.txt"
words_file = open(path, 'r')
words = words_file.readlines()

filtered_words = []
print("Original dictionary length:", len(words))

for word in words:
    word = word.replace("á", "a", -1).replace("é", "e", -1).replace("í", "i", -1).replace("ó", "o", -1).replace("ú", "u", -1)
    if word.strip().endswith(("er", "ir", "ar", "-", "arse", "mente")) or word.strip().startswith("-") or word.find(" ") > -1:
        continue
    elif word.strip().endswith(("a", "e", "o")):
        word = word.strip() + "s\n"
    elif word.strip().endswith(("ad", "al", "el", "ol", "on", "u", "i")):
        word = word.strip() + "es\n"
    elif word.strip().endswith("ez"):
        word = word.strip()[:-1] + "ces\n"
    filtered_words.append(word)

print("Filtered dictionary length:", len(filtered_words))

path = Path(__file__).parent / "../raw/filtered_words.txt"
with open(path, "w") as txt_file:
    for word in filtered_words:
        txt_file.write(word)
