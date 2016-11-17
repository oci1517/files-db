import os

words = []

fileno = input("Numéro de fichier à charger [1/2/3] : \n").strip() or '1'
filepath = os.path.join("tjwordlist/english/words-{}.txt".format(fileno))

with open(filepath, "r") as fd:
    words = [w.strip() for w in fd if w.strip() != '']

anagrams = {}

for w in words:
    anagram_code = ''.join(sorted(w))

    if anagram_code in anagrams:
        anagrams[anagram_code].append(w)
    else:
        anagrams[anagram_code] = [w]

for anagram_list in anagrams.values():
    if len(anagram_list) >= 2:
        print("Sont des anagrames : ", " / ".join(anagram_list))
