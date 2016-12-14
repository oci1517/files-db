import os

# variables globales
words = []
anagrams = {}

def load_words(filepath):
    # mettre tous les mots (un mot par ligne) dans la liste ``words`` en supprimant
    # les sauts de lignes finaux avec .strip()
    with open(filepath, "r") as fd:
        words = [w.strip().lower() for w in fd if w.strip() != '']

    for w in words:
        # les mots qui sont des anagrammes les uns des autres auront tous le même
        # "anagram_code"
        anagram_code = ''.join(sorted(w))

        if anagram_code in anagrams:
            anagrams[anagram_code].append(w)
        else:
            anagrams[anagram_code] = [w]

def decode(encoded_word):
    anagram_code = "".join(sorted(encoded_word))
    if anagram_code in anagrams:
        decoded_word_list = anagrams[anagram_code]
        # S'il n'y a pas d'amiguité
        if len(decoded_word_list) == 1:
            decoded_word = decoded_word_list[0]
        # gestion des ambiguités ... on met les possibilités séparées par le
        # caractère |
        else:
            decoded_word = "|".join(decoded_word_list[0])

    else:
        decoded_word = encoded_word
    return decoded_word

def do_it(ciphered_message):
    encoded_words = ciphered_message.split()
    decoded_words = []

    for w in encoded_words:
        decoded_words += [decode(w)]

    return " ".join(decoded_words)

def main():
    filepath = "tjwordlist/english/words-1.txt"
    coded_message = input("Saisir le texte crypté par anagramme (anglais) : ")
    # Si l'utilisateur n'a rien saisi dans l'entrée
    coded_message = coded_message or "IINFHS SOLOHC AEMK SIWREKOFR"

    load_words(filepath)
    decoded_message = do_it(coded_message.lower())

    print("Message décrypté : ", decoded_message)

main()
