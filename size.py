# Tweets are limited to 280 characters for standard accounts 
# and 25000 for premium accounts.


premium = None
# while premium is not assigned a value
while premium == None:
    # ask if premium or not yes no question; then remove spaces and change to lowercase
    answer = input("Do you have X Premium? (y/n) ").strip().lower()
    # process input
    if answer in ["y", "yes"]:
        premium = True
    elif answer in ["n","no"]:
        premium = False
    else: # print error message and restart loop
        print("Invalid input.")

# ask for a tweet
tweet = input("Enter a tweet: ") 

# count characters
char_count = len(tweet)

# check against length limits
if (char_count > 280 and not premium) or char_count > 25000:
    print("Too long.")
else:
    words = tweet.split()
    plural = ""
    num_words = len(words)
    # include plural s if # words is not 1
    if num_words != 1:
        plural = "s"

    # print result
    print("Your tweet is " + f'{len(words)} word{plural} long.')