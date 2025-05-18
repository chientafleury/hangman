import random

words = ["python", "programming", "hangman", "game"]
word = random.choice(words)
guesses = []
attempts = 6

while attempts > 0:
    display = [letter if letter in guesses else "_" for letter in word]
    print(" ".join(display))
    
    if "_" not in display:
        print("Kamu menang!")
        break
    
    guess = input("Tebak huruf: ").lower()
    if guess in guesses:
        print("Sudah ditebak!")
    elif guess in word:
        guesses.append(guess)
    else:
        attempts -= 1
        print(f"Salah! Sisa nyawa: {attempts}")
else:
    print(f"Game over! Kata yang benar: {word}")