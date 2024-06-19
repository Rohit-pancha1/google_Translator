from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    # Get the source text from the text widget
    source_text = source_txt.get("1.0", END).strip()
    if source_text:
        # Translate the text
        translator = Translator()
        translation = translator.translate(source_text, src=source_lang.get(), dest=target_lang.get())
        target_txt.delete("1.0", END)
        target_txt.insert(END, translation.text)

# Initialize the main window
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='#FA8072')

# Title label
title_label = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
title_label.place(x=100, y=40, height=50, width=300)

# Source language label
source_label = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black")
source_label.place(x=10, y=100, height=30, width=200)

# Source language selection
source_lang = ttk.Combobox(root, values=list(LANGUAGES.values()), state='readonly')
source_lang.place(x=220, y=100, height=30, width=150)
source_lang.set("english")  # default source language

# Source text widget
source_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
source_txt.place(x=10, y=140, height=200, width=480)

# Target language label
target_label = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), fg="Black")
target_label.place(x=10, y=360, height=30, width=200)

# Target language selection
target_lang = ttk.Combobox(root, values=list(LANGUAGES.values()), state='readonly')
target_lang.place(x=220, y=360, height=30, width=150)
target_lang.set("spanish")  # default target language

# Target text widget
target_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
target_txt.place(x=10, y=400, height=200, width=480)

# Translate button
translate_btn = Button(root, text="Translate", font=("Times New Roman", 20, "bold"), command=translate_text)
translate_btn.place(x=200, y=620, height=50, width=200)

# Start the main loop
root.mainloop()
