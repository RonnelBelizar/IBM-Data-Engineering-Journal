# Sample Word Lookup

def count(word, string):
    count_little = 0
    for words in string.lower().split():
        if words == word.lower():
            count_little += 1
    print(f"{word}: {count_little}")


count("mary", "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go")
