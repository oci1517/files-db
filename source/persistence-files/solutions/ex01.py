import os

words = []

# Choisir le fichier dictionnaire à charger
fileno = input("Numéro de fichier à charger [1/2/3] : \n").strip() or '1'
filepath = os.path.join("tjwordlist/english/words-{}.txt".format(fileno))

# mettre tous les mots (un mot par ligne) dans la liste ``words`` en supprimant
# les sauts de lignes finaux avec .strip()
with open(filepath, "r") as fd:
    words = [w.strip() for w in fd if w.strip() != '']

# Les clés de ce dictionnaire seront des "anagram_codes" : en effet, si l'on
# prend un mot et que l'on trie toutes ses lettres dans l'ordre alphabétique, on
# obtient un même mot "anagram_code" pour tous les mots qui sont des anagrames
# les uns des autres ==> relation d'équivalence. Les valeurs de ce dictionnaire
# seront des listes de mots qui sont tous équivalents entre eux (anagrammes les
# uns des autres)
anagrams = {}

for w in words:
    # les mots qui sont des anagrammes les uns des autres auront tous le même
    # "anagram_code"
    anagram_code = ''.join(sorted(w))

    if anagram_code in anagrams:
        anagrams[anagram_code].append(w)
    else:
        anagrams[anagram_code] = [w]

for anagram_list in anagrams.values():
    if len(anagram_list) >= 2:
        print("Sont des anagrames : ", " / ".join(anagram_list))
