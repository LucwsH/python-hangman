import random

with open("words.txt", "r", encoding="utf-8") as file:
    words = [word.strip() for word in file.read().split(",")]

random_word = random.choice(words)
random_word_length = len(random_word)

attempts = 7
display_word = "_" * random_word_length
correct_letters = []

print(f"Sua palavra tem {random_word_length} letras: {display_word}")
print("Digite uma letra para iniciar.")

def get_letter_occurrence(word, letter):
    return word.lower().count(letter.lower())

while attempts > 0:
    letter = input("Letra ou palavra: ").strip()

    if letter.lower() == random_word.lower():
        print(f"Você acertou, a palavra era {random_word}!")
        break

    if len(letter) > 1:
        print("Utilize uma letra!")
        continue

    if letter.lower() in correct_letters:
        print(f"A letra '{letter}' já foi utilizada.")
        continue

    occurrences = get_letter_occurrence(random_word, letter)

    if occurrences < 1:
        attempts -= 1
        print(f"Errou! Ainda há: {attempts} chances.")
        continue

    display_word_list = list(display_word)

    for i in range(len(random_word)):
        if random_word[i].lower() == letter.lower():
            display_word_list[i] = random_word[i]

    display_word = "".join(display_word_list)
    correct_letters.append(letter.lower())

    print(f"Acertou uma letra! {display_word}")

    if display_word == random_word:
        print(f"Você acertou, a palavra era {random_word}!")
        break
else:
    print("Acabaram suas tentativas!")
