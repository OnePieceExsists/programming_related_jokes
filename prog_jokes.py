import pyjokes
import tkinter as tk

def show_joke():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)

root = tk.Tk()
root.title("Programming Joke")
root.geometry("400x200")

joke_label = tk.Label(root, text="Click the button for a joke!", wraplength=300, font=("Arial", 12))
joke_label.pack(pady=10)

joke_button = tk.Button(root, text="Get a Joke", command=show_joke)
joke_button.pack(pady=10)

root.mainloop()