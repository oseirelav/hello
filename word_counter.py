# Prompt for a word or multiple and then prompt for a paragraph 
# and then count number of the word in the paragraph

words = []
enter_word = True

# initialize loop
while True:
    if enter_word:
        # prompt word
        word = input("Please enter a word: ")
        if word not in words:
            words.append(word)
    # ask if user wants to add more words
    cont = input("Would you like to add more words? (y/n) ").strip().lower()
    if cont in ["y","yes"]:
        enter_word = True
        continue
    elif cont in ["n","no"]:
        break
    else:
        enter_word = False

# prompt paragraph
paragraph = input("Please enter a paragraph: ")

# split paragraph into separate words
paragraph = paragraph.split()

# loop through all words and count
for i in range(0,len(words)):
    print(f"There are {paragraph.count(words[i])} {words[i]}'s in the paragraph.")

    
