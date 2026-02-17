import tkinter as tk
from tkinter import messagebox

from word_counter import count_words


def open_word_counter():
    win = tk.Toplevel(root)
    win.title("Word Counter")

    tk.Label(win, text="Enter a sentence:").pack(anchor="w", padx=8, pady=(8, 0))
    text = tk.Text(win, height=4, width=50)
    text.pack(padx=8, pady=4)

    result_frame = tk.Frame(win)
    result_frame.pack(fill="x", padx=8, pady=8)

    word_lbl = tk.Label(result_frame, text="Words: -")
    word_lbl.pack(anchor="w")
    char_lbl = tk.Label(result_frame, text="Chars (no spaces): -")
    char_lbl.pack(anchor="w")
    long_lbl = tk.Label(result_frame, text="Longest word: -")
    long_lbl.pack(anchor="w")

    def analyze():
        sentence = text.get("1.0", "end").strip()
        try:
            res = count_words(sentence)
        except ValueError:
            messagebox.showwarning("Input error", "Please enter a non-empty sentence.")
            return

        word_lbl.config(text=f"Words: {res['word_count']}")
        char_lbl.config(text=f"Chars (no spaces): {res['char_count']}")
        long_lbl.config(text=f"Longest word: {res['longest_word']}")

    tk.Button(win, text="Analyze", command=analyze).pack(pady=(0, 8))


root = tk.Tk()
root.title("Word Counter")

tk.Label(root, text="Word Counter", font=(None, 12, "bold")).pack(padx=12, pady=(12, 6))
tk.Button(root, text="Open Word Counter", width=20, command=open_word_counter).pack(pady=6)

tk.Button(root, text="Quit", width=10, command=root.quit).pack(pady=(12, 12))

root.mainloop()
