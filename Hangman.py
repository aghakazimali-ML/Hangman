import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------
# WORD LIST + DRAWINGS
# ---------------------------
HANGMAN_PICS = [
    "",  # unused (to make step numbers easier)
    "Base",
    "Pole",
    "Top Beam",
    "Rope",
    "Head",
    "Body",
    "Left Arm",
    "Right Arm",
    "Left Leg",
    "Right Leg"
]

WORDS = ["Kazim", "ImranKhan", "BabarAzam", "developer", "internet", "Hangman"]


# ==========================================================
# FUNCTION: Creates the actual Hangman Game Window
# ==========================================================
def show_hangman_window():
    game = tk.Toplevel()      # <-- second window (not root)
    game.title("Hangman Game")
    game.geometry("500x600")

    # Game Variables
    secret_word = random.choice(WORDS)
    guessed = set()
    tries = tk.IntVar(value=0)

    # Canvas
    canvas = tk.Canvas(game, width=300, height=300, bg="white")
    canvas.pack(pady=20)

    # Convert secret word to blanks
    def get_display_word():
        return " ".join([letter if letter in guessed else "_" for letter in secret_word])

    word_label = tk.Label(game, text=get_display_word(), font=("Arial", 24))
    word_label.pack(pady=10)

    entry = tk.Entry(game, font=("Arial", 18), width=5)
    entry.pack()

    message = tk.Label(game, text="Wrong Tries: 0", font=("Arial", 16))
    message.pack(pady=10)

    # DRAW HANGMAN
    def draw_hangman(step):
        if step == 1:
            canvas.create_line(20, 280, 280, 280, width=3)
        elif step == 2:
            canvas.create_line(80, 280, 80, 40, width=3)
        elif step == 3:
            canvas.create_line(80, 40, 200, 40, width=3)
        elif step == 4:
            canvas.create_line(200, 40, 200, 80, width=3)
        elif step == 5:
            canvas.create_oval(180, 80, 220, 120, width=3)
        elif step == 6:
            canvas.create_line(200, 120, 200, 190, width=3)
        elif step == 7:
            canvas.create_line(200, 140, 170, 170, width=3)
        elif step == 8:
            canvas.create_line(200, 140, 230, 170, width=3)
        elif step == 9:
            canvas.create_line(200, 190, 170, 230, width=3)
        elif step == 10:
            canvas.create_line(200, 190, 230, 230, width=3)

    # GUESS LOGIC
    def guess_letter():
        letter = entry.get().lower()
        entry.delete(0, tk.END)

        # Validation
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid", "Enter ONE letter!")
            return

        if letter in guessed:
            messagebox.showinfo("Oops", "You already tried that!")
            return

        guessed.add(letter)

        # Correct Guess
        if letter in secret_word:
            word_label.config(text=get_display_word())

            if "_" not in get_display_word():
                messagebox.showinfo("Winner", "You Win!")
                guess_button.config(state="disabled")
            return

        # Wrong Guess
        tries.set(tries.get() + 1)
        wrong = tries.get()
        message.config(text=f"Wrong Tries: {wrong}")
        draw_hangman(wrong)

        if wrong == 10:
            messagebox.showerror("Game Over", f"Word was: {secret_word}")
            guess_button.config(state="disabled")

    guess_button = tk.Button(game, text="Guess", font=("Arial", 16), command=guess_letter)
    guess_button.pack(pady=10)


# ==========================================================
# MAIN LAUNCHER WINDOW
# ==========================================================
root = tk.Tk()
root.title("Hangman Launcher")
root.geometry("300x200")

btn = tk.Button(root, text="Start Hangman", font=("Arial", 16), command=show_hangman_window)
btn.pack(pady=40)

root.mainloop()
