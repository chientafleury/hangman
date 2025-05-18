import random
from english_words import get_english_words_set

# ASCII Art untuk Hangman (7 stages, termasuk awalnya kosong)
hangman_graphics = [
    """
     ------
     |    |
          |
          |
          |
          |
    ========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    ========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    ========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    ========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    ========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    ========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    ========
    """
]


def generate_random_word(min_len=4, max_len=8):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choices(chars, k=random.randint(min_len, max_len)))

def play_hangman():
    # Pilih kata secara acak
    # Ambil daftar kata (web2 = kamus umum)
    word_list = get_english_words_set(['web2'], lower=True)
    secret_word = random.choice(list(word_list))
    guessed_letters = []
    attempts_left = 6  # 6 nyawa
    hangman_stage = 0  # Index untuk gambar hangman

    print("\n--- Selamat Datang di Game Hangman! ---")
    print("Tebak huruf untuk menyelamatkan si Hangman!")
    print(hangman_graphics[hangman_stage])

    # Main loop
    while attempts_left > 0:
        # Tampilkan kata dengan huruf yang sudah ditebak
        display = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("\nKata: " + ' '.join(display))

        # Input pemain
        guess = input("Tebak huruf: ").lower()

        # Validasi input
        if len(guess) != 1 or not guess.isalpha():
            print("Masukkan hanya 1 huruf!")
            continue

        # Cek jika huruf sudah ditebak sebelumnya
        if guess in guessed_letters:
            print("Kamu sudah menebak huruf ini!")
            continue

        guessed_letters.append(guess)

        # Cek apakah huruf ada di kata rahasia
        if guess in secret_word:
            print("Benar!")
        else:
            attempts_left -= 1
            hangman_stage += 1
            print(f"Salah! Sisa nyawa: {attempts_left}")
            print(hangman_graphics[hangman_stage])

        # Cek jika menang
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nSelamat! Kamu menang! Kata yang benar: {secret_word.upper()}")
            break

    # Jika kalah
    if attempts_left == 0:
        print(hangman_graphics[6])  # Gambar hangman lengkap
        print(f"\nGame Over! Kata yang benar: {secret_word.upper()}")


# Mulai game
play_hangman()
