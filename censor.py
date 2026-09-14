# Prompt for a word to replace, a word to replace it with, 
# and a paragraph, and then replace the words.

word_pairs = dict()

enter_word = True

while True:
    if enter_word:
        # prompt for word
        word = input("Enter a word to replace: ")
        replace = input(f"Enter a word to replace {word} with: ")
        word_pairs[word] = replace
    # prompt to continue
    cont = input("Would you like to continue adding words to the censor? (y/n) ").strip().lower()
    if cont in ["y","yes"]:
        enter_word = True
        continue
    elif cont in ["n","no"]:
        break
    else:
        enter_word = False
        print("Invalid input.")

# prompt for paragraph
paragraph = input("Please enter a paragraph: ")

# get keys in dictionary
keys = list(word_pairs.keys())

# replace words
for i in range(0, len(keys)):
    paragraph = paragraph.replace(keys[i], word_pairs[keys[i]])

# print result
print(paragraph)

# drawback is .replace() replaces every instance of the object 
# even if it is not an isolated word (i.e. "the" and "there")