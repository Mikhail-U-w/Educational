def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        wordl = word.lower()
        root_wordl = root_word.lower()
        if (root_wordl in wordl) or (wordl in root_wordl):
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)