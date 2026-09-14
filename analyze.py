# Combine previous tasks.

name = input("Hello! What is your name? ")

words = []
enter_word = True
while True:
    if enter_word:
        word = input(f"{name}, please give me a word to count: ")
        if word not in words:
            words.append(word)
    cont = input(f"{name}, would you like to add more words to count? (y/n) ").strip().lower()
    if cont in ['y','yes']:
        enter_word = True
        continue
    elif cont in ['n','no']:
        break
    else:
        print('Invalid input.')
        enter_word = False

paragraph = input(f"{name}, please give me a paragraph: ")

print(f"Total character count is {len(paragraph)}.")
paragraph = paragraph.split()
print(f"Total word count is {len(paragraph)}.")

for word in words:
    count = paragraph.count(word)
    plural = ""
    verb = "is"
    if count != 1:
        plural = "s"
        verb = "are"
    print(f"There {verb} {count} {word}{plural} in the paragraph.")
