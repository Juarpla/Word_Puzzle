"""
Student: Juan Plasencia
*Showing Creativity:
-We started with a list of topics, then randomly selected a topic and finally selected a random word from the selected list.
"""
#Showing Creativity radom list of topics
import random

topics = ["cities", "countries", "colors", "jobs"] 
topic = random.choice(topics)
if topic == "cities":
    cities = ["vancouver", "chicago", "cuzco", "cartagena", "charleston"]
    secret_word = random.choice(cities)
elif topic == "countries":
    countries = ["peru", "usa", "india", "rusia", "japon", "china"]
    secret_word = random.choice(countries)
elif topic == "colors":
    colors = ["blue", "orange", "red", "green", "black"]
    secret_word = random.choice(colors)
else:
    jobs = ["engineer", "doctor", "teacher", "accountant"]
    secret_word = random.choice(jobs)

print(f"\nWelcome to the word guessing game 😎 , Topic: {topic}!\n")

#Hint: Number of letters
print(f"Your hint is 😋 : ", end=" ")
for underscore in secret_word:
    print("_ ", end="")

#Asking the guess word and get the lenght of the entered word
lenght_word = False
number_tries = 0
while lenght_word == False:
    guess_word = input("\nWhat is your guess? ").lower()
    if len(secret_word) != len(guess_word) and guess_word != secret_word:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    #verifying matching letters
    elif len(secret_word) == len(guess_word) and guess_word != secret_word:
        #print about the letter founded and index matched     
        print("Your hint is 😮 :", end=" ")
        for i in range(len(guess_word)):
            letter = guess_word[i] 
            found = False 
            for j in range(len(secret_word)): 
                if letter == secret_word[j]: 
                    found = True 
                    if i == j: 
                        print(letter.upper(), end=" ") 
                    elif i != j: 
                        print(letter.lower(), end=" ") 
            if not found: 
                print("_ ", end="") 
    #Game Over
    else:
        lenght_word = True
        print("Congratulations 🥳 ! You guessed it!")
    #Calculating the number of attempts per cycle
    number_tries = number_tries + 1

#Showing the number of attempts
if number_tries == 1:
    print(f"it took you {number_tries} guess 😏 .")
else:
    print(f"it took you {number_tries} guesses 😄 .")