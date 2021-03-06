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
    elif word.strip().endswith(("al", "able", "ible", "ador", "oro", "ito", "sio", "iso", "imo", "ivo", "ense", "eso", "aco", "ado", "ante", "orio")):
        filtered_words.append(word)

print("Singular dictionary length:", len(filtered_words))

path = Path(__file__).parent / "../raw/singular_words.txt"
with open(path, "w") as txt_file:
    for word in filtered_words:
        txt_file.write(word)
