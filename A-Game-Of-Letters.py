san = input().split()

vowels = ["a", "e", "i", "o", "u"]

new_sentence = ""

for word in san:

    new_word = ""
    length = len(word)

    for i in range(length):
        if word[i].lower() in vowels:
            new_word = word[i:] + new_word
            break
        else:
            new_word += word[i]
    new_sentence += new_word + " "

print(new_sentence)